import os
from dotenv import load_dotenv
from pathlib import Path


# Config env variable
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


PROJECT_NAME = os.getenv('PROJECT_NAME')
DATABASE_URL = os.getenv('DATABASE_URL')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
SUMMARY_TEMPLATE_ID = os.getenv('SUMMARY_TEMPLATE_ID')
