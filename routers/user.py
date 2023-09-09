
from database import SessionLocal, get_db,db
from models import User
from fastapi import  APIRouter, Depends, Request
from main import send_email,app
from _celery.task import send_previous_letters
router = APIRouter(
    prefix="/users",
    tags=['Users']
)

def get_all_emails():
    emails = db.query(User).get("email")
    return emails




@router.post("/users/")
async def create_user(request: Request, db: SessionLocal = Depends(get_db)):
    form_data = await request.form()
    name = form_data.get("name")
    email = form_data.get("email")
    work_subject = form_data.get("work_subject")
    if not name or not email or not work_subject:
        return "Invalid data"
    
    all_mails=get_all_emails()
    if email in all_mails:
        return "Invalid data"
    send_previous_letters(email,work_subject)
    user = User(name=name, email=email, work_subject=work_subject)
    db.add(user)
    db.commit()
    send_email("User Registration", f"Hello {name},\nYou have successfully registered as a user.\nYour work subject is {work_subject}.")
    return "User created successfully"

