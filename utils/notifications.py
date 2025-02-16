import os
import smtplib
from email.message import EmailMessage
import logging
from dotenv import load_dotenv

load_dotenv()


def send_email_alert(subject, body, to_email):
    """
    Sends an email alert using the SMTP configuration.

    :param subject: Email subject.
    :param body: Email body content.
    :param to_email: Recipient email address.
    """
    try:
        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = int(os.getenv("SMTP_PORT", "587"))
        smtp_user = os.getenv("SMTP_USER")
        smtp_password = os.getenv("SMTP_PASSWORD")
        from_email = smtp_user

        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        logging.info("Email alert sent successfully.")
    except Exception as e:
        logging.error(f"Error sending email: {e}")
