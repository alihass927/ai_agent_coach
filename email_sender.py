import smtplib
from email.message import EmailMessage
import os

def send_email(subject, body, to_email):
    sender = to_email
    password = os.getenv("GMAIL_APP_PASSWORD")

    if not password:
        raise ValueError("GMAIL_APP_PASSWORD not set")
    
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content("Yuor Email client does not support HTML")
    msg.add_alternative(body, subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
        