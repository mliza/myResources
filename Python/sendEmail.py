#!/usr/local/bin/python3.7
"""
    Author: Martin E. Liza 
    Date:   10/16/2019 
    File:   sendingEmail.py 
    Def:    Send emails to a specified email address every 30 [s]

    ex. ./sendingEmail.py &


    Author             Date           Revision  
    --------------------------------------------------
    Martin E. Liza     10/16/2019     Initial Version  
""" 

# NOTE: 
#       - Requires python3 
#       - This currently works for a gmail account, search 'CONFIGURE ME' 
#         and configure that line to make it work with another email 
#       - Environmental variables called EMAIL_USER and EMAIL_PASS 
#         must be created in your .bashrc 
#       - Less secure app access on the sending email must be turned off
#         https://myaccount.google.com/lesssecureapps?pli=1
#       - Search 'CONFIGURE ME' to set up your own receiving email, email 
#         subject and email body 
#       - To automatically delete the emails being send to your gmail see 
#         link https://www.youtube.com/watch?v=uqJwPvYdCRA

import os 
import smtplib
import schedule 
import time 
from email.message import EmailMessage 

def sendingEmail(subject, body, receiverEmailAdd):   
    """ 
        This function sends an email to 
        a designated email address 

        subject = string, email's subject 
        body = string, email's body 
    """
    # Setup  
    msg = EmailMessage() 
    msg['From'] = os.environ.get('EMAIL_USER') 
    msg['To'] = receiverEmailAdd
    msg['Subject'] = subject  
    msg.set_content(f'{body}')

    # Login into the server and sends email 
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:  #CONFIGURE ME - change server   
            smtp.login(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASS')) 
            smtp.send_message(msg) 	    

# CONFIGURE ME - to my own subject, body and receiver email  
def scheduleJob(): 
    """
        This function calls sendingEmail(subject, body, recieverEmailAdd)  
    """
    subject = 'configureMeToDeleteOnGmail' 
    body = 'Test' 
    receiverEmailAdd = 'mliza@email.arizona.edu'
    sendingEmail(subject, body, receiverEmailAdd) 

# Invoke Functions 
if __name__ == "__main__":
    # Schedule function to run every 30 [s] 
    schedule.every(30).seconds.do(scheduleJob)

    # Needed to run forever 
    while True: 
        schedule.run_pending() 
        time.sleep(1)
