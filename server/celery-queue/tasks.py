import os
from celery import Celery
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name="tasks.email")
def send_email(email, subject, message):
  message = Mail(
    from_email="addr@example.com",
    to_emails=email,
    subject=subject,
    html_content=f'<p>{message}</p>'
  )
  try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    return response.status_code
  except Exception as e:
    print(e)
    return "Error sending email"