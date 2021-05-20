alpha = "abcdefghijklmnopqrstuvwxyz"
key =   "xznlwebgjhqdyvtkfuompciasr"
message = input("enter the message : ")
cipher = ""
for i in message:
    cipher+=key[alpha.index(i)]
print(cipher)