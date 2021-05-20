# Question 3: Write a program that asks the user to enter a word and then capitalizes every other letter of that word. So if the user enters Rashid, the program should print rAsHiD.
string= input("input a string")
string1 = string[::2].lower()
string2 = string[1::2].upper()
for i in range(len(string)):
    if i % 2 == 0:
        print(string1[i//2], end="")
    else:
        print(string2[i//2], end="")
