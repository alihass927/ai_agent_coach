from email_sender import send_email

send_email(
    subject="Test Gmail",
    body="Test Gmail SMTP",
    to_email="ali.hass927@gmail.com"
)

print("sent")