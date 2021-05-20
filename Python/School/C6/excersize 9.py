s = input("input a decimal number")
if "." in s:
    print(s[s.index(".")+1:])
else:
    print("that doesnt have a decimal point")