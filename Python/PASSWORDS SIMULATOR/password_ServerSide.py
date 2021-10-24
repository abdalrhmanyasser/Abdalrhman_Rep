import random
import smtplib, ssl
import string
import HASHING
from email.message import EmailMessage
def compare(email, hashed_pass):
    try:
        file = open("D:\\Visual Code\\Abdalrhman_Rep\\Python\\PASSWORDS SIMULATOR\\EMAIL_DATA_BASE.DTF", "rt")
    except:
        file = open("D:\\Visual Code\\Abdalrhman_Rep\\Python\\PASSWORDS SIMULATOR\\EMAIL_DATA_BASE.DTF", "x")
        file.close()
        file = open("D:\\Visual Code\\Abdalrhman_Rep\\Python\\PASSWORDS SIMULATOR\\EMAIL_DATA_BASE.DTF", "rt")

    content = file.readlines()
    if content != []:
        for line in content:
            if (email == line.split("\t")[0]):
                if (hashed_pass == line.split("\t")[1]):
                    if (Send_auth()):
                        return True
    return False

def SignUp_Client(email, hashed_pass):
    try:
        file = open("D:\\Visual Code\\Abdalrhman_Rep\\Python\\PASSWORDS SIMULATOR\\EMAIL_DATA_BASE.DTF", "at")
    except:
        file = open("D:\\Visual Code\\Abdalrhman_Rep\\Python\\PASSWORDS SIMULATOR\\EMAIL_DATA_BASE.DTF", "x")
        file.close()
        file = open("D:\\Visual Code\\Abdalrhman_Rep\\Python\\PASSWORDS SIMULATOR\\EMAIL_DATA_BASE.DTF", "at")
    if not email in file.read():
        file.write("\n" + email + "\t" + hashed_pass)

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "dev.abdalrhman@gmail.com"  # Enter your address
receiver_email = "abdalrhman.yasser6e@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")

def Send_auth():


    smtp_server = "smtp.gmail.com"
    sender_email = "dev.abdalrhman@gmail.com"
    receiver_email = "abdalrhman.yasser6e@gmail.com"
    code = (''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)))
    message = """your Special Authentication Code is : """ + code
    port = 465  # For SSL
    password = "5E3^I$TUpPKDA$bu"

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Code for Python Messaging'
    msg['From'] = sender_email
    msg['To'] = receiver_email


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg)
    User_given_code = input("what is the code")
    if User_given_code == code:
        return True
    else:
        return False
