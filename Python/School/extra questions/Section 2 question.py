string=input("enter a string")
print(len(string))
print(string*5)
print(string[0])
print(string[-1])
print(string[: :-1])
if len(string) >= 7:
    print(string[6])
else:
    print("please enter more than 7 charecters next time")
print(string[1:-1])
print(string.upper())
print(string.replace('a', 'e'))
print('*'*len(string))