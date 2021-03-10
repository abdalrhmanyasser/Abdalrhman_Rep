for i in range(1600, 2025):
    if (i % 4 == 0 and (i % 100 != 0 or i % 400 == 0)):
        print(i)