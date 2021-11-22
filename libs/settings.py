from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(verbose=True)
#cp .env.example .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


OPEN_URL = os.getenv('OPEN_URL')
OPEN_APP_KEY = os.getenv('OPEN_APP_KEY')
OPEN_SECRET_KEY = os.getenv('OPEN_SECRET_KEY')


MOLOG_USERNAME = os.getenv('MOLOG_USERNAME')
MOLOG_PASSWORD = os.getenv('MOLOG_PASSWORD')

