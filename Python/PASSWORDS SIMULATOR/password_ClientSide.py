from HASHING import *
from password_ServerSide import *


def main():
    print("""Select what you want to do:
    1) Sign In
    2) Sign up""")
    x = input("")
    if int(x) == 1:
        SignIn()
    elif int(x) == 2:
        SignUp()
def SignIn():
    _email = input("Please Enter Your Email:\n")
    _password = input("Please Enter Your Password\n")
    if (compare(_email, hash(_password))):
        print("Hello")

def SignUp():
    SignUp_Client(input("Please Enter Your Email:\n"), hash(input("Please Enter Your Password\n")))

main()
