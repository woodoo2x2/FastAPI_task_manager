import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.settings import Settings


class MailClient:
    def __init__(self, settings: Settings):
        self.from_email = settings.MAIL_FROM
        self.smtp_server = settings.MAIL_SERVER
        self.smtp_port = settings.MAIL_PORT
        self.smtp_password = settings.MAIL_PASSWORD

    def send_mail(self, to: str) -> None:
        msg = self.__build_message("Welcome mail", "Welcome to the mail system", to)
        self.__send_mail(msg)

    def __build_message(self, subject: str, body: str, to: str) -> MIMEMultipart:
        msg = MIMEMultipart()

        msg['From'] = self.from_email
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        return msg

    def __send_mail(self, msg: MIMEMultipart) -> None:
        context = ssl.create_default_context()
        servet = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port,context=context)
        servet.login(self.from_email, self.smtp_password)
        servet.send_message(msg)
        servet.close()