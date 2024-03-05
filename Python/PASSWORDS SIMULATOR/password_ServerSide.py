import random
import string
import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
from email.mime.text import MIMEText
def compare(email, hashed_pass):
    try:
        file = open("C:\\Users\\abdal\\Documents\\Visual Code\\Abdalrhman_Rep\\Python\\PASSWORDS SIMULATOR\\EMAIL_DATA_BASE.DTF", "rt")
    except:
        file = open("C:\\Users\\abdal\\Documents\\Visual Code\\Abdalrhman_Rep\\Python\\PASSWORDS SIMULATOR\\EMAIL_DATA_BASE.DTF", "x")
        file.close()
        file = open("C:\\Users\\abdal\\Documents\\Visual Code\\Abdalrhman_Rep\\Python\\PASSWORDS SIMULATOR\\EMAIL_DATA_BASE.DTF", "rt")

    content = file.readlines()
    if content != []:
        for line in content:
            if (email == line.split("\t")[0]):
                if (hashed_pass == line.split("\t")[1]):
                    if (Send_auth(email)):
                        return True
    return False

def SignUp_Client(email, hashed_pass):
    try:
        file = open("C:\\Users\\a+bdal\\Documents\\Visual Code\\Abdalrhman_Rep\\Python\\PASSWORDS SIMULATOR\\EMAIL_DATA_BASE.DTF", "a+")
    except:
        file = open("C:\\Users\\abdal\\Documents\\Visual Code\\Abdalrhman_Rep\\Python\\PASSWORDS SIMULATOR\\EMAIL_DATA_BASE.DTF", "x")
        file.close()
        file = open("C:\\Users\\abdal\\Documents\\Visual Code\\Abdalrhman_Rep\\Python\\PASSWORDS SIMULATOR\\EMAIL_DATA_BASE.DTF", "a+")
    if not email in file.read():
        file.write("\n" + email + "\t" + hashed_pass)

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "dev.abdalrhman@gmail.com"  # Enter your address
receiver_email = "abdalrhman.yasser6e@gmail.com"  # Enter receiver address

SCOPES = [
        "https://www.googleapis.com/auth/gmail.send"
    ]
def Send_auth(email):

    
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    service = build('gmail', 'v1', credentials=creds)
    code = (''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)))
    message = MIMEText("""your Special Authentication Code is : """ + code)
    message['to'] = email
    message['subject'] = 'Code for Python Messaging'
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    try:
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(F'An error occurred: {error}')
    
    User_given_code = input("what is the code")
    if User_given_code == code:
        return True
    else:
        return False
