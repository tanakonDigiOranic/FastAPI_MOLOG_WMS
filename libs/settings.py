from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(verbose=True)
#cp .env.example .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
# REDIS_PORT = os.getenv('REDIS_PORT', '6379')

OPEN_URL = os.getenv('OPEN_URL')
OPEN_APP_KEY = os.getenv('OPEN_APP_KEY')
OPEN_SECRET_KEY = os.getenv('OPEN_SECRET_KEY')
OPEN_ACCESS_KEY = os.getenv('OPEN_ACCESS_KEY')
TIMESTAMP = os.getenv('TIMESTAMP')
API_CODE = os.getenv('API_CODE')
MOLOG_USERNAME = os.getenv('MOLOG_USERNAME')
MOLOG_PASSWORD = os.getenv('MOLOG_PASSWORD')
