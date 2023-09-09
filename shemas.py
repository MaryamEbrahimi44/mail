from pydantic import BaseModel, EmailStr
from datetime import datetime


class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

class Email(BaseModel):
    email: EmailStr
    subject: str
    content: str
    created_at: datetime