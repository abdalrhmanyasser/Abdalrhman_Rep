i = int(input("Enter the year right now"))
if (i % 4 == 0 and (i % 100 != 0 or i % 400 == 0)):
    print(i)