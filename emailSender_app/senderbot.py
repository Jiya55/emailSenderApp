import smtplib
import ssl
from email.message import EmailMessage
from datetime import *
import time
#email password = yrrktuvkmjtekuhy
def email_sender_bot(email_sender, email_sender_password, email_receiver, subject, body, sending_time = None):
    email_creator = EmailMessage()
    email_creator['From'] = email_sender
    email_creator['To'] = email_receiver
    email_creator['Subject'] = subject
    email_creator.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_sender_password)
        if sending_time != None:
            send_time = datetime.strptime(sending_time,  '%b %d %Y %I:%M%p') # set your sending time in UTC
            time.sleep(send_time.timestamp() - time.time())
            smtp.sendmail(email_sender, email_receiver, email_creator.as_string())
            return 
        smtp.sendmail(email_sender, email_receiver, email_creator.as_string())