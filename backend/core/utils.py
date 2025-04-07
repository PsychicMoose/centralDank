from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()  # ⬅️ this loads your .env file into the environment

def send_sms(message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")
    to_number = os.getenv("MY_PHONE_NUMBER")

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    )
    return message.sid

