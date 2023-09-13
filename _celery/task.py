from models import Letter,User
from datetime import datetime
from worker import celery
from main import send_email
from database import db
from datetime import datetime, timedelta

@celery.periodic_task(run_every=celery.schedules.crontab(minute=0, hour='*/4'))
def send_new_letters():  
    now = datetime.datetime.now()
    four_hours_ago = now - datetime.timedelta(hours=4)
    letters = db.query(Letter).filter(Letter.created_at >= four_hours_ago).all()
    for letter in letters:
        subject = letter.subject
        body = letter.body 
        receiver = db.query(User.email).join(Letter, User.work_subject == Letter.subject).all()
        send_email(subject, body,receiver)



@celery.task
def send_previous_letters(email,work_subject):

    last_month = datetime.utcnow() - timedelta(days=30)

     # Query the letters that were created in the last month
    letters = db.query(Letter).filter(Letter.created_at >= last_month,Letter.subject==work_subject).all()

    for letter in letters:
        subject = letter.subject
        body = letter.body
        send_email(subject, body,email)
