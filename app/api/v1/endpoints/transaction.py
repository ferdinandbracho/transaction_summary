from fastapi import (
    APIRouter,
    Response,
    Depends,
    status,
    UploadFile
)
from  app.models import summary as Sy
from app.schemas.summary import Summary
from app.db.session import engine
import pandas as pd
from app.db.session import get_db
from app.utils import list_sum, list_avg, month_counter


Sy.Base.metadata.create_all(bind=engine)

# Init router
router = APIRouter()


@router.post('/import', status_code=status.HTTP_200_OK)
async def import_csv_transactions(
    response: Response,
    file: UploadFile,
    db=Depends(get_db),
):
    """

    ## **Upload transactions history csv:**

    **Return:**

        if success execution:
            - http 200 ok
            - Obj with
                - Nested obj with a summary[success count, errors count]

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

    # Formatting the return dict
    upload_result = {
        'summary': {
            'total_balance': 0,
            'avg_debit': 0,
            'avg_credit': 0,
            'number_transactions': {},
        }
    }

    # Init needed variables
    records = rfile.to_dict('records')
    debit_list = [x['Transaction'] for x in records if x['Transaction'] > 0]
    credit_list = [x['Transaction'] for x in records if x['Transaction'] < 0]
    dates = [x['Date'] for x in records]

    # Setting data to send email and save in db
    total_debit = list_sum(debit_list)
    total_credit = list_sum(credit_list)
    total_balance = total_debit + total_credit
    avg_debit = list_avg(debit_list)
    avg_credit = list_avg(credit_list)
    month_transactions = month_counter(dates)

    # Setting Summary obj
    summary = Sy.Summary(
        total_balance = round(total_balance, 2),
        avg_debit = avg_debit,
        avg_credit = avg_credit,
        month_transactions = month_transactions
    )

    db.add(summary)
    db.commit()

    for a in db.query(Sy.Summary).all():
        print(a)


    return
    db.add(record_to_create)

    db.flush()

    return f'-{total}'
    db.commit()

    # setting finales data to return
    upload_err_results['summary']['success_total_count'] = success_counter
    upload_err_results['summary']['errors_total_count'] = error_counter

    return upload_err_results