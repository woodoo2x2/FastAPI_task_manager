from sqlalchemy import Column, Integer, String

from database import Base
class UserProfile(Base):
    __tablename__ = 'userprofile'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
