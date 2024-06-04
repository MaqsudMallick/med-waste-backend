import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

sender_email = "YOUR_EMAIL@outlook.com"
receiver_email = "RECEIVER@gmail.com"
password = "YOUR_PASSWORD"
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Med waste Notification"
body = "Dustbin is filled with waste. Please replace it."
msg.attach(MIMEText(body, 'plain'))

def send_email():
    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)  
        server.starttls()  
        server.set_debuglevel(1)  
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully")
        server.quit()
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
        if 'Connection unexpectedly closed' in str(e):
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    return True

def send_notif():
    max_retries = 3
    for attempt in range(max_retries):
        if send_email():
            break
        else:
            print(f"Retrying... ({attempt + 1}/{max_retries})")
            time.sleep(5)  
    if attempt == max_retries - 1:
        print("Failed to send email after multiple attempts")
        return False
    return True
