import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import dotenv_values


class EmailSender:
    def __init__(self):
        config = dotenv_values(".env")
        self.smtp_server = config.get("SMTP_HOST")
        self.smtp_port = config.get("SMTP_PORT")
        self.smtp_user = config.get("SMTP_USER")
        self.smtp_password = config.get("SMTP_PASSWORD")
        self.smtp_from = config.get("MAIL_FROM")
        self.smtp_auth = config.get("SMTP_AUTH")
        self.smtp_recipient = config.get("MAIL_RECIPIENT")

    def send_email(self, subject, body):
        message = MIMEMultipart()
        message['From'] = self.smtp_from
        message['To'] = self.smtp_recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            if self.smtp_auth == "SSL":
                server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.sendmail(self.smtp_user, self.smtp_recipient.split(","), message.as_string())