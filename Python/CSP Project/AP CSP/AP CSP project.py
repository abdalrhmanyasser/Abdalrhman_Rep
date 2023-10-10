import random
import os.path

# defining global variables
FilePath = ""
passwords = {}

def viewPasswords(websiteNameOnly = True, numbered = False, passwordDict: dict = passwords) -> None:
    """
    A Function that displays the passwords passed from the `passwordDict` with flags `websiteNameOnly` and `numbered` to customize the looks
    """
    if len(passwordDict) >= 1:
        userChoice = input("Do you want to view the health score of your passwords type y for yes anything else for no\nYour Choice : ")
        if userChoice.lower() == "y": healthScore = True
        else: healthScore = False

        # loop over the dictionary and add each customizable thing based on the flags
        for passwordIndex in range(len(passwordDict)):
            output = ""
            if numbered:
                output+=str(passwordIndex+1) + ". "
            if websiteNameOnly:    
                output += list(passwordDict.keys())[passwordIndex]
            else:
                output += list(passwordDict.keys())[passwordIndex] + " : " + passwordDict[list(passwordDict.keys())[passwordIndex]]
            if healthScore:
                output += "\thealth : " + str(passwordHealth(passwordDict[list(passwordDict.keys())[passwordIndex]]))
            print(output)
    else:
        print("there are no passwords to display")
        
def createPassword() -> None:
    """
    A function that prompts the user to create an entry in the passwords Dictionary
    """
    # take the input for the website name
    while True:
        websiteName = input("Enter the website's name\n(if you wnat to cancel type \"Cancel\")\nYour Choice: ")
        if websiteName.lower() == "cancel":
            return
        if " " not in websiteName:
            break
        else:
            print("You cant include spaces in website names")
    # take input for password, available choices are randomize and custom password
    while True:
        userChoice = input("Enter the password for the given website\n* If you want a strong password to be generated type _generate_\n* If you want to cancel type \"Cancel\"\nYour Choice : ")
        if userChoice.lower() == "cancel":
                return
        if userChoice.lower() == "_generate_":
            length = None
            while True:
                length = input("type how long you want the password to be : ")
                if length.isnumeric() and 0 < int(length):
                    break
                else:
                    print("length must be a number and greater than 0")
            
            password = generate_password(int(length))
            print("your new password for {} is {}".format(websiteName, password))
            # save the generated data to the dictionary
            passwords[websiteName] = password
            break
        # error checking if user inputs a space as part of their password where the key is the website name and the value is the password
        elif " " not in userChoice:
            print("your new password for {} is {}".format(websiteName, userChoice))
            # save data to the dictionary where the key is the website name and the value is the password
            passwords[websiteName] = userChoice
            break
        else:
            print("you cant include spaces in the password")

def generate_password(length:int=12) -> str:
    """
    A function that generates a random password of a given length.
    """
    # list of characters to choose from
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password
def passwordHealth(password: str) -> int:
    """
    return an int which represents the "health" of the `password` given
    """
    health = 0
    # check the password for its strength and add point  based on what is included
    if len(password) > 8:
        health += len(password)-6
    for i in "!@#$%^&*()":
        if i in password:
            health+=1
    hasNumber = False
    for letter in password:
        if letter in "1234567890":
            hasNumber = True
    if hasNumber:
        health += 1
    if password.lower() != password and password.upper() != password:
        health += 2
    return health

def deletePassword():
    """
    Prompt the user to delete a website and password combination
    """
    # error checking so that we dont try to delete a non existant thing
    if len(passwords) >= 1:
        # show options
        print("options : ")
        viewPasswords(websiteNameOnly=True, numbered=True)
        # take the user input while checking for errors and giving the user the ability to cancel
        while True:
            userChoice=input("Enter a number ranging from (1-"+str(len(passwords)) + ") (if you want to cancel write \"Cancel\") : ")
            if userChoice.isnumeric() and 0 < int(userChoice) <= len(passwords):
                passwords.pop(list(passwords.keys())[int(userChoice)-1])
                break
            elif userChoice.lower() == "cancel":
                break
            else:
                print("please enter a valid number")
    else:
        print("There are no passwords to delete")

def LoadData() -> None:
    """
    Load Previously Exported Data
    """
    while True:
        try:
            FileLocation = input("Enter the file name (write Cancel if you want to cancel) : ")
            if FileLocation.lower() == "cancel":
                break
            file = open(FileLocation, "rt")
            for line in file.readlines():
                passwordAndWebsite = line.replace("\n", "").split(" ")
                passwords[passwordAndWebsite[0]] = passwordAndWebsite[1]
            file.close()
            break
        except FileNotFoundError:
            print("please enter a correct File Directory")
        except IndexError:
            print("the file you tried to load has been corrupted")
            break

def ExportData() -> None:
    """
    a function that saves the data from the passwords dictionary to a file specified by the user
    """
    while True:
        # try opening the file and write the data to it
        FileLocation = input("Enter the file name (write \"Cancel\" if you want to cancel) : ")
        if FileLocation.lower() == "cancel":
            return
        # use the os.path lib to check if the file exists
        if os.path.exists(FileLocation):
            file = open(FileLocation, "wt")
            data = ""
            # Access the data to get exported
            for password in passwords:
                data+=password + " " + passwords[password]+"\n"
            file.write(data)
            file.close()
            break
        else:
            print("File doesn't exist!")

# only start the program if the file is started directly rather than imported
if __name__ == "__main__":
    while True:
        print("\nmain menu : ")
        print("\t1. View Websites saved\n\t2. View Passwords\n\t3. Create Password\n\t4. Delete Password\n\t5. Export To File\n\t6. Load Data\n\t7. Exit")
        userChoice = input("Your Choice : ")
        # checking for if the input is a number so that it doesnt break the system
        if userChoice.isnumeric() and 0 < int(userChoice) <= 7 :
            match int(userChoice):
                case 1:
                    viewPasswords(websiteNameOnly=True, numbered=False)
                case 2:
                    viewPasswords(websiteNameOnly=False, numbered=False)
                case 3:
                    createPassword()
                case 4:
                    deletePassword()
                case 5:
                    ExportData()
                case 6:
                    LoadData()
                case 7:
                    exit()
        else:
            print("you must give a number between 0 and 6")
