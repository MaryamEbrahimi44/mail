from database import SessionLocal, get_db
from models import  Letter
from main import send_email
from fastapi import  APIRouter, Depends, Request


router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/letters/")
async def create_letter(request: Request, db: SessionLocal = Depends(get_db)):
    form_data = await request.form()
    subject = form_data.get("subject")
    body = form_data.get("body")
    if not subject or not body:
        return "Invalid data"
    letter = Letter(sender="email.service547@gmail.com", subject=subject, body=body)
    db.add(letter)
    db.commit()
    send_email("Letter Submission", f"Hello,\nYou have successfully submitted a letter.\nThe subject is {subject}.\nThe body is {body}.")  
    return "Letter created successfully"
