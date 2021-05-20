s1 = input("first String : ")
s2 = input("second String : ")
if len(s1) == len(s2):
    for i in range(len(s1)):
        print(s1[i], s2[i], end="", sep="")
else:
    print("the string lengths dont match up")