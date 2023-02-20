# Trasanction Summary Maker

System dedicated to create summaries of transactions.

**Live API** (Documentation and testing) -> http://54.151.11.102/docs#/

## **Features**
- CSV file upload
- Summary based on csv data
- Database log
- Sending summary by email
- List summaries history


## **Stack**
- Python
- FastApi
- SQLAlchemy
- SQLite
- Pydantic
- Pandas
- Sendgrid
- Swagger
- Docker
- AWS ec2


## **Details**
FastApi project, currently with two endpoints:
- **/import** - Endppoint dedicated to import valid csv file to analyze and summarize data, if user emails is provided then this endpoint triggers an email sender with the summarized data

    - This endpoint validate 1)if files is valid, 2)also if is a csv and 3)lastly if the column structure if the expected, in any of this case the error is indicated to the user
    - When procss csv is success it create a database entry and response this data to the user, send email with summary to indicated email (optional)
   ### **Resnpose Body **
   -  ``` json
        // Response and  log in database
        {
            "id": 1,
            "user_email": "ferdinand.bracho@gmail.com",
            "avg_credit": -15.38,
            "total_balance": 39.74
            "avg_debit": 35.25,
            "month_transactions": {
                "July": 2,
                "August": 2
            },
            "created_at": "2023-02-20T14:20:28.484615",
        }
        ```


  ### **Email Tempalte**
  - ![Email](https://github.com/ferdinandbracho/transaction_summary_maker/blob/cde121f5a2f9f861188bc235ff13a476804a6db3/docs_img/Screenshot%20from%202023-02-20%2008-26-46.png)

- **/List** - Endppoint dedicated to retrieve a list of summaries logs in database
    - ``` json
            // List response
        [
            {
                "id": 1,
                "user_email": "ferdinand.bracho@gmail.com",
                "total_balance": 39.74,
                "avg_debit": 35.25,
                "avg_credit": -15.38,
                "month_transactions": {
                    "July": 2,
                    "August": 2
                    },
                "created_at": "2023-02-20T14:20:28.484615"
            },
            {
                "id": 2,
                "user_email": "whatacupset@gmail.com",
                "total_balance": 39.74,
                "avg_debit": 35.25,
                "avg_credit": -15.38,
                "month_transactions": {
                    "July": 2,
                    "August": 2
                    },
                "created_at": "2023-02-20T14:33:52.636210"
            },
            {
                "id": 3,
                "user_email": "test_email_user@gmail.com",
                "total_balance": 39.74,
                "avg_debit": 35.25,
                "avg_credit": -15.38,
                "month_transactions": {
                    "July": 2,
                    "August": 2
                    },
                "created_at": "2023-02-20T14:34:10.213871"
            }
        ]
        ```

## Execute Locally
- Prerequisite:
    - Python +3.9
    - Docker +23
- Clone de Repository
- Run:
    ``` sh
    docker compose up --build
    ```
- After the build of the "docker" image, creation and execution of the container the user can go to http://0.0.0.0:8000/docs to the interactive openApi documentation and test "endpoints" from there, also can run request on the server from any client (Web, mobile or an app like postman)
- [Test CSV](https://github.com/ferdinandbracho/transaction_summary_maker/blob/0bf4dd6ba3dcf627160c6220ed0a1dac4ec27910/test.csv)

## RoadMap
- Connect to postgres db - *since we currently use sqlite this is just a minor tweak*
- Adding extra validation to csv data, e.g Validate if all transactions data are valid numbers, of if the transactions id are unique
- Change the deploy architecture, instead of using a server in AWS EC2, change to a serverless approach and use AWS LAMBDA
    - S3 Post/Put Trigger to call the function
    - Use [Magnun](https://pypi.org/project/magnum/) python package to prepare handler
- Create web client to test api integration (to create summaries and to list then)

## Extra Note
- *Waiting for twilio sendgrid account restoration*
- The integration is complete but for some reason sendgrid ask for extra information about the usage of the account, is already provided by the developer but still under revision
 ![integration Complete](https://github.com/ferdinandbracho/transaction_summary_maker/blob/fd38b59a0bc45163f588a07d16250475396298cb/docs_img/Screenshot%20from%202023-02-20%2009-10-28.png)
