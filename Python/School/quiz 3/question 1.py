x = eval(input("Enter amount of credit"))
if (x <=25):
    print("Freshman")
elif 25 < x < 50:
    print("Sophamore")
elif 50 < x < 75:
    print("Juniors")
elif x > 76:
    print("Seniors")
else:
    print("cant be negative")