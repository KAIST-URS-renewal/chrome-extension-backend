import os
from dotenv import load_dotenv

# find the directory in which the current file resides
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# take environment variables from ./.config/.env file
load_dotenv(os.path.join(BASE_DIR, ".config", ".env"))

# Check if all needed environment variables are set
POSTGRES_DB_PORT = os.environ.get('POSTGRES_DB_PORT')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_DB_USER = os.environ.get('POSTGRES_DB_USER')
POSTGRES_DB_PASSWORD = os.environ.get('POSTGRES_DB_PASSWORD')
POSTGRES_DB_TS = os.environ.get('POSTGRES_DB_TS')

if ((not POSTGRES_DB) or (not POSTGRES_DB_TS) or (not POSTGRES_DB_PORT) or (not POSTGRES_DB_USER) or (not POSTGRES_DB_PASSWORD)):
    raise Exception("Environment variables are not properly set.")

# set POSTGRES_DB_URL
os.environ["POSTGRES_DB_URL"] = f'postgresql://{POSTGRES_DB_USER}:{POSTGRES_DB_PASSWORD}@localhost:{POSTGRES_DB_PORT}/{POSTGRES_DB}'
