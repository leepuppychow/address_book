import os
from celery import Celery
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

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

@celery.task(name="tasks.text_message")
def send_text(number, message):
  text_message = twilio_client.messages.create(
    body=message,
    from_=f"+{TWILIO_PHONE_NUMBER}",
    to=number
  )
  return text_message.sid
