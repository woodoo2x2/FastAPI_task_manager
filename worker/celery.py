import smtplib
import ssl
from email.mime.multipart import MIMEMultipart

from celery import Celery

from app.settings import Settings

celery = Celery(__name__)
settings = Settings()

celery.conf.broker_url = settings.CELERY_REDIS_URL
celery.conf.result_backend = settings.CELERY_REDIS_URL


@celery.task(name='send_email_task')
def send_email(msg: MIMEMultipart):
    context = ssl.create_default_context()
    servet = smtplib.SMTP_SSL(settings.smtp_server, settings.smtp_port, context=context)
    servet.login(settings.from_email, settings.smtp_password)
    servet.send_message(msg)
    servet.close()
