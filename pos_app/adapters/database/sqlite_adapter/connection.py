import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
database = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
schema = os.getenv('DB_SCHEMA', 'public')

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"options": f"-c search_path=dbo,{schema}"})

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()