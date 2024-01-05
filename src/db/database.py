import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = os.environ.get('POSTGRES_DB_URL')

## create connection to postgresql
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, vind=engine)

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

