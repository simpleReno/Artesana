import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
database = os.getenv('DB_NAME')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')

SQLALCHEMY_DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()
