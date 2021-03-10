temp = int(input("What is the temperture"))
mode = input("F or C")
if str.upper(mode) == "F":
    print("the temperture in C is", (5/9)*(temp-32))
elif str.upper(mode) == "C":
    print("the temperture in F is", (9/5)*(temp+32))