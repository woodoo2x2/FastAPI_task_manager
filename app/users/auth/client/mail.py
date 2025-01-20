from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.settings import Settings
from worker.celery import send_email_task


class MailClient:
    def __init__(self, settings: Settings):
        self.from_email = settings.MAIL_FROM
        self.smtp_server = settings.MAIL_SERVER
        self.smtp_port = settings.MAIL_PORT
        self.smtp_password = settings.MAIL_PASSWORD

    def send_mail(self, to: str) -> None:
        subject = "Welcome mail"
        body = "Welcome to the mail system"
        send_email_task.delay(self.from_email, to, subject, body)

