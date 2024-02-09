import logging
import os

from sqlalchemy import create_engine, Engine
from sqlalchemy.exc import SQLAlchemyError

DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "3306")

DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def connect_db() -> Engine | None:
    try:
        engine = create_engine(DB_URL)
        logging.info(f"Connected to database: {DB_URL}")
        return engine
    except SQLAlchemyError as e:
        logging.error(e)
        return None
