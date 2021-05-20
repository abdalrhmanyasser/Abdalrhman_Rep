# Question 1: Write a program that asks the user to enter a string. The program should then print the following:
# a)     The total number of characters in the string
# b)    The string repeated 10 times
# c)     The first character of the string
# d)    The first three characters of the string
# e)     The last three characters of the string
# f)      The string backwards
# g)     The seventh character of the string if the string is long enough and a message otherwise
# h)    The string with its first and last characters removed
# i)      The string in all caps
# j)      The string with every a replaced with an e
# k)    The string with every character replaced by an *
string=input("enter a string")
print(len(string))
print(string*10)
print(string[0])
print(string[0:3])
print(string[-3:])
print(string[: :-1])
if len(string) >= 7:
    print(string[7])
else:
    print("the string is shorter than 7 charecters")
print(string[1:-1])
print(string.upper())
print(string.replace('a', 'e'))
print('*'*len(string))