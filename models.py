from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from database import Base 

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    work_subject = Column(String)


class Letter(Base):
    __tablename__ = "letters"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)
    subject = Column(String)
    body = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
