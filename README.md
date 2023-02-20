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
- **/import** - Dedicated to import valid csv file to analyze and summarize data, if user emails is provided then this endpoint triggers an email sender with the summarized data

    - Validated if files is valid, also if is a csv and lastly if the column structure if the expected, in any of this case the error is indicated to the user
    - When success create a database entry and response this to the user and send email with summary to indicated email (optional)
    - ``` json
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

  - [Email](docs_img/Screenshot from 2023-02-20 08-26-46.png)

- **/List** - Dedicated to retrieve a list of summaries logs in database
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
- After the build of the docker image and creation and execution of the container user can go to http://0.0.0.0:8000