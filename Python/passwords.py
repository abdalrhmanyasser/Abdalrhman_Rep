from hashlib import sha256
def checkPassword():
    i = 5
    signedIn = False
    while i != 0 and not signedIn:
        print("you have "+str(i)+" tries left")
        hashed = sha256(input().encode('utf-8'))
        if hashed.hexdigest() == "44fddd8b9d8755a392567bc5a7f54a5dcee0a82c2f19fa1c3afc808bca6cc841":
            signedIn = True
            print("Welcome")
        i-=1
checkPassword()