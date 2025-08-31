from smtplib import SMTP_SSL
from dotenv import load_dotenv
import os
from datetime import datetime as dt


load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SENDER_GMAIL_ADDRESS = os.getenv("SENDER_GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
PORT = os.getenv("PORT")
RECIPIENT_EMAIL_ADDRESS = os.getenv("RECIPIENT_EMAIL_ADDRESS")


def send_email(address, info):

    with SMTP_SSL(SMTP_SERVER, PORT) as smtp:
        smtp.login(SENDER_GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        date_string = f"{dt.now().strftime('%a, %d %b %Y %H:%M:%S %z')}+0000"
        msg = (
            f"From: {SENDER_GMAIL_ADDRESS}\r\n"
            f"To: {RECIPIENT_EMAIL_ADDRESS}\r\n"
            f"Subject: Sunderland Bin Collection Information - {address}\r\n"
            f"Date: {date_string}\r\n"
            "MIME-Version: 1.0\r\n"
            "Content-Type: text/plain; charset=utf-8\r\n"
            "\r\n"
            f"{info}\r\n"
        )
        smtp.sendmail(
            from_addr=SENDER_GMAIL_ADDRESS,
            to_addrs=RECIPIENT_EMAIL_ADDRESS,
            msg=msg
        )
