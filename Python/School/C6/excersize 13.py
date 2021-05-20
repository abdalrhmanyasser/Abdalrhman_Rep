import math as m

if input("do you want to encrypt a message : (y/n) ").lower() == "y":
    message = input("what is the message : ")
    print(message[0::2]+message[1::2])
else:
    message = input("what is the message : ")
    for i in range(m.ceil(len(message)/2)):
        print(message[i],end="")
        if len(message) > m.ceil(len(message)/2)+i:
            print(message[m.ceil(len(message)/2)+i],end="")
