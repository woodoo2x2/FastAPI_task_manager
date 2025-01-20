
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from celery import Celery
from app.settings import Settings

celery = Celery(__name__)
settings = Settings()

celery.conf.broker_url = settings.CELERY_REDIS_URL
celery.conf.result_backend = settings.CELERY_REDIS_URL
celery.conf.update(
    broker_connection_retry_on_startup=True  # Исправляет предупреждение
)

@celery.task(name='send_email_task')
def send_email_task(from_email: str, to_email: str, subject: str, body: str):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(settings.MAIL_SERVER, settings.MAIL_PORT, context=context) as server:
            server.login(from_email, settings.MAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        raise Exception(f"Failed to send email: {e}")
