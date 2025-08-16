from smtplib import SMTP_SSL
from dotenv import load_dotenv
import os


load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
USERNAME = os.getenv("SMTP_USERNAME")
PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
PORT = os.getenv("PORT")

with SMTP_SSL(SMTP_SERVER, PORT) as smtp:
    smtp.set_debuglevel(1)
    smtp.login(USERNAME, PASSWORD)
    msg = (
    f"From: {EMAIL_ADDRESS}\r\n"
    f"To: {EMAIL_ADDRESS}\r\n"
    "Subject: Test\r\n"
    "Date: Fri, 16 Aug 2025 12:00:00 +0000\r\n"
    "MIME-Version: 1.0\r\n"
    "Content-Type: text/plain; charset=utf-8\r\n"
    "\r\n"
    "This is a test email."
    )
    smtp.sendmail(
        from_addr=EMAIL_ADDRESS,
        to_addrs=EMAIL_ADDRESS,
        msg=msg
        )