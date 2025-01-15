from sqlalchemy import Column, Integer, String

from app.database.database import Base
class UserProfile(Base):
    __tablename__ = 'userprofile'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    name = Column(String)
    google_access_token = Column(String)
    yandex_access_token = Column(String)