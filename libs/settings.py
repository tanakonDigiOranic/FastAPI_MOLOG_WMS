from dotenv import load_dotenv
from pathlib import Path
import datetime
import os

load_dotenv(verbose=True)
#cp .env.example .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def TimestampMillisec64():
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)


OPEN_URL = os.getenv('OPEN_URL')
OPEN_APP_KEY = os.getenv('OPEN_APP_KEY')
OPEN_SECRET_KEY = os.getenv('OPEN_SECRET_KEY')


MOLOG_USERNAME = os.getenv('MOLOG_USERNAME')
MOLOG_PASSWORD = os.getenv('MOLOG_PASSWORD')


SIGN_CODE_SYSTEM_TOKEN = os.getenv('SIGN_CODE_SYSTEM_TOKEN')
SIGN_CODE_REFRESH_TOKEN = os.getenv('SIGN_CODE_REFRESH_TOKEN')
SIGN_CODE_SKU = os.getenv('SIGN_CODE_SKU')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
