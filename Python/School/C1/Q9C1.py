x = int(input("Enter the meal price in AED: "))
y = int(input("Enter the tip you want to leave : "))
print("Total (tip unincluded) : " + str(x) + "\nTip : " + str(y) + "%" + "\nTotal (tip included) : " + str(x+x*(y/100)) + "AED")