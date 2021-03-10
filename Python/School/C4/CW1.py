mark = eval(input("what is your mark?"))
if mark >= 90:
    print("A")
elif 70 < mark < 90:
    print("B")
elif 60 < mark < 70:
    print("C")
elif 60 > mark:
    print("F")
else:
    print("Invalid")