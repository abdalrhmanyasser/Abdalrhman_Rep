# Question 2: Write a program that asks the user to enter a word and determines whether the word is a palindrome or not. A palindrome is a word that reads the same backwards as forwards.

string=input("input a string")
if string == string[::-1]:
    print("yes that was a palendrom")
else:
    print("no that isnt a palendrom")