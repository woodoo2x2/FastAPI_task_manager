from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

import sqlite3
from settings import Settings

Settings = Settings()

engine = create_engine(f"sqlite:///{Settings.DATABASE_NAME}")

Session = sessionmaker(engine)
def get_db_session():
    return Session
