s = input("enter a string with the letter a\n")
if "a" in s:
    print(s[:s.index("a")+1])
    print(s[s.index("a")+1:])
else:
    print("the string doesnt have the letter a in it")
