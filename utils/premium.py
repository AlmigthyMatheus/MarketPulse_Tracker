# utils/premium.py
import uuid
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def generate_premium_code():
    """
    Generates a unique premium access code (8-character string).
    """
    return str(uuid.uuid4()).upper()[:8]

def send_premium_code_email(recipient_email, premium_code):
    """
    Sends an email with the premium access code to the recipient.
    """
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")

    subject = "Your Premium Access Code for MarketPulse Tracker"
    body = f"Thank you for your purchase! Your premium access code is: {premium_code}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        print("Premium code sent successfully.")
    except Exception as e:
        print(f"Error sending premium code email: {e}")
