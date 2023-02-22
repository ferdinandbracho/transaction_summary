from fastapi import (
    APIRouter,
    Response,
    Depends,
    status,
    UploadFile
)
from  app.models import summary as Sy
from app.schemas.summary import SummaryItem
from app.db.session import engine
import pandas as pd
from typing import List
from app.db.session import get_db
from app.utils import list_sum, list_avg, month_counter, send_email
import app.config as config



Sy.Base.metadata.create_all(bind=engine)

# Init router
router = APIRouter()


@router.post('/import', status_code=status.HTTP_200_OK)
async def import_csv_transactions(
    response: Response,
    file: UploadFile,
    user_email: str = None,
    db=Depends(get_db),
):
    """

    ## **Upload transactions history csv and send account summary if email:**

    **Query params:**

        user_email:
            str: optional valid email to send account summary

    **Return:**

        if success execution:
            - http 200 ok
            - Obj with summary data

        if fail execution:
            - http 400 Bad request
            - Code internal error
                - ER01: File cant be read
                - ER02: Incorrect file not csv
                - ER03: Invalid csv structure

    """
    # Trying to read the file
    try:
        open('/tmp/file', 'wb').write(await file.read())
    except Exception:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return 'Error 01 - Invalid File: Cannot read'

    # Validating viability
    viability_res = ''

    # Trying to read the file as csv
    try:
        rfile = pd.read_csv('/tmp/file')
    except Exception:
        viability_res = 'ER02: Incorrect file not csv'
        return f'Invalid: {viability_res}'

    # Validating df columns structure
    columns = [
        'id',
        'Date',
        'Transaction',
    ]

    df_cols = rfile.columns

    for i in range(len(df_cols)):
        if columns[i] != df_cols[i]:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return  'ER03: Invalid csv structure'


    # Init needed variables
    records = rfile.to_dict('records')
    debit_list = [x['Transaction'] for x in records if x['Transaction'] > 0]
    credit_list = [x['Transaction'] for x in records if x['Transaction'] < 0]
    dates = [x['Date'] for x in records]

    # Setting data to send email and save in db
    total_debit = list_sum(debit_list)
    total_credit = list_sum(credit_list)
    summary_data = {
        'total_balance' : round(total_debit + total_credit, 2),
        'avg_debit' : list_avg(debit_list),
        'avg_credit' : list_avg(credit_list),
        'month_transactions' : month_counter(dates),
    }

    # Setting Summary obj
    summary = Sy.Summary(
        user_email = user_email,
        total_balance = summary_data['total_balance'],
        avg_debit = summary_data['avg_debit'],
        avg_credit = summary_data['avg_credit'],
        month_transactions = summary_data['month_transactions']
    )


    # Send to db
    db.add(summary)
    db.commit()

    # If user email send email
    if user_email:
        send_email(
            to_email=user_email,
            subject='Account summary',
            template_id=config.SUMMARY_TEMPLATE_ID,
            data=summary_data
            )

    print(summary)
    return summary


@router.get(
    '/list',
    status_code=status.HTTP_200_OK,
)
async def get_summary_history(
    response: Response,
    db = Depends(get_db)
) -> List[SummaryItem]:
    """
    ## Retrieve summary history

    **Return:**

        List of summaries
    """

    try:
        # Search for all summaries
        Summaries = db.query(Sy.Summary).all()
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "description": "Server Error",
            "exception": str(e)
        }

    res = []

    for summary in Summaries:
        res.append(SummaryItem(
            id=summary.id,
            user_email=summary.user_email,
            total_balance = summary.total_balance,
            avg_debit = summary.avg_debit,
            avg_credit = summary.avg_credit,
            month_transactions = summary.month_transactions,
            created_at=summary.created_at
        ))

    return res