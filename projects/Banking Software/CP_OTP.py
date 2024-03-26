# import smtplib
# from email.message import EmailMessage
import base64
import smtplib
from email.message import EmailMessage
import random

def send_otp(r):
    sender = "ronil.theamazing@gmail.com"
    receiver = r
    password = "gfapdputusthxjsa"
    subject = "Verify your password."
    otp = str(random.randint(10000, 99999))
    body = '''Hello RonilBanksCo User,

    If have not signed up for Ronil Banks, ignore this message and report it as spam.

    Below is your OTP for verifying password change.

    OTP: %s
    ''' %otp

    message = EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, 'Hi')
    print('Sent')

send_otp("shivamphulari030@gmail.com")