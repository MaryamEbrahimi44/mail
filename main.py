import uvicorn
import smtplib
from email.mime.text import MIMEText
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from _celery import worker
from routers import letter,user


app = FastAPI()

templates = Jinja2Templates(directory="templates")

async def send_email(subject, body,receiver):
    sender = "email.service547@gmail.com"
    receiver = receiver
    subject = subject
    body = body
    msg = MIMEText(body)
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("email.service547@gmail.com", "@mail1234")
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()
    


app.include_router(letter.router)
app.include_router(user.router)


if __name__ == "__main__": 
    uvicorn. run(app, host="0.0.0.0", port=8000)

    worker.celery.worker_main(['worker', '--loglevel=info'])