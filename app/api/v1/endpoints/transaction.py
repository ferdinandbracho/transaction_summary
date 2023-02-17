from fastapi import (
    APIRouter,
    Response,
    Depends,
    status,
    UploadFile
)
from app.schemas.summary import Summary
import pandas as pd
from app.db.session import get_db

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

    # validating df columns structure
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

    # format return
    upload_result = {
        'summary': {
            'total_balance': 0,
            'avg_debit': 0,
            'avg_credit': 0,
            'number_transactions': {},
        }
    }

    # init counters
    row = 1
    records = rfile.to_dict('records')
    total = 0

    # iterate through each record to analyze and validate
    for r in records:
        row += 1
        fail_validation = False

        if r['Transaction'] < 0:
            total -= r['Transaction']


    # {'id': 1, 'Date': '7/15', 'Transaction': 60.5}
    # {'id': 2, 'Date': '8/2', 'Transaction': -61.5}
    # {'id': 3, 'Date': '8/13', 'Transaction': 62.5}

        continue

        db.add(record_to_create)

        db.flush()

    return f'-{total}'
    db.commit()

    # setting finales data to return
    upload_err_results['summary']['success_total_count'] = success_counter
    upload_err_results['summary']['errors_total_count'] = error_counter

    return upload_err_results