import sqlite3
from settings import Settings

Settings = Settings()


def get_db_connection():
    a = sqlite3.connect(Settings.DATABASE_NAME)
    print(a)
    a.close()
