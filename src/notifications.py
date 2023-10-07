```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, to_email):
    from_email = "your_email@gmail.com"
    password = "your_password"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def send_confirmation(user_profile, order):
    subject = "UMI Order Confirmation"
    message = f"Hello {user_profile['name']},\n\nYour order for {order['meal']} has been placed and will be delivered to {user_profile['address']}.\n\nThank you,\nUMI"
    send_email(subject, message, user_profile['email'])

def send_notification(user_profile, order, eta):
    subject = "UMI Order Notification"
    message = f"Hello {user_profile['name']},\n\nYour order for {order['meal']} has been placed and will be delivered in approximately {eta} minutes.\n\nThank you,\nUMI"
    send_email(subject, message, user_profile['email'])
```