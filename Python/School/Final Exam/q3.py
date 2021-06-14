inp1 = input("Enter the first String")
inp2 = input("Enter the second String")
print("string #1 before replacement : " + inp1, "string #2 before replacement : " + inp2, sep="\n")
str1 = inp2[0] + inp1[1:]
str2 = inp1[0] + inp2[1:]
print("string #1 After replacement : " + str1, "string #2 After replacement : " + str2, sep="\n")
