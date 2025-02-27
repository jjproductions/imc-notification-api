from fastapi import HTTPException
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .schemas import NotificationRequest
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

#def send_email(subject: str, body: str, to_email: str):
def send_email(request: NotificationRequest) -> bool:
    try:
        # Set up the email server
        server = smtplib.SMTP(os.getenv("EMAIL_SMTP_SERVER"), os.getenv("EMAIL_SMTP_PORT"))
        server.starttls() # Secure the connection
        server.login(os.getenv("EMAIL_USERNAME"), os.getenv("EMAIL_PASSWORD"))


        subject = request.emailInfo.subject
        body = request.emailInfo.body
        to_email = request.email
    
        
        print(datetime.now())
        print (f'Email: FROM {os.getenv("EMAIL_USERNAME")}')
        print (f'Email: TO {to_email}')
        print (f'App Password: {os.getenv("EMAIL_PASSWORD")}')
        msg = MIMEMultipart()
        msg["From"] = os.getenv("EMAIL_USERNAME")
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        # and send the email
        
        # Settings to send mail via Azure
        # server.set_debuglevel(1)  # Enables detailed debugging
        # server.ehlo()
        # auth_string = f'user={os.getenv("EMAIL_USERNAME")}\1auth=BEARER {os.getenv("AZURE_APP_TOKEN")}'
        # server.docmd("AUTH", "XOAUTH2 " + auth_string)
        
        # print(f'Sending email from {os.getenv("EMAIL_USERNAME")} with password {os.getenv("EMAIL_PASSWORD")}')
        # print(f'Sending email to {to_email}')
        server.sendmail(os.getenv("EMAIL_USERNAME"), to_email, msg.as_string())
        
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        server.quit()
        return False

def send_sms(body: str, to_phone: str):
    try:
        # Set up the Twilio client and send the SMS
        # client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        # client.messages.create(
        #     body=body,
        #     from_=os.getenv("TWILIO_PHONE_NUMBER"),
        #     to=to_phone
        # )
        return True
    except Exception as e:
        print(f"Failed to send SMS: {e}")
        return False

def verify_api_key(api_key: str) -> bool:
    print(f'Header: {api_key}')
    print(os.getenv("API_KEY"))
    return api_key == os.getenv("API_KEY")

def verify_card_id_email(card_id: int, email: str) -> bool:
    # Query the database to verify the card ID and email
    return True