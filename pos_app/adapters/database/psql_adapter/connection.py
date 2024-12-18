import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from dotenv import load_dotenv
load_dotenv()

from pos_app.core.domain.logs.logger import setup_loggers
log_queries, log_connections, log_orm = setup_loggers()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
database = os.getenv('DB_NAME')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')

SQLALCHEMY_DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)

def get_engine():
    return engine

@contextmanager
def get_session():
    engine = get_engine()
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()
