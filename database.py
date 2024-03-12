from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DB_PORT, DB_HOST, DB_NAME,DB_PASS,DB_USER

DATABASE_URL='postgresql://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:5432/%(DB_NAME)s'
engine=create_engine(DATABASE_URL, echo=True)
Base=declarative_base()
Session=sessionmaker()