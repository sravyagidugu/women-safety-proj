import smtplib
from email.message import EmailMessage

def send_email_alert(subject, body, to_email):
    sender_email = "lokanadam@gmail.com"
    sender_password = "your_password"

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print("Alert Sent!")

# Example Usage
send_email_alert("Women Safety Alert", "Threat detected! Please take action.", "recipient@gmail.com")
