count4 = 0
count9 = 0
for i in range(101):
    if (i*i) % 10 == 4:
        count4+=1
        print(i, "with a square : ", i*i, "ends in 4")
    if (i*i) % 10 == 9:
        count9+=1
        print(i, "with a square : ", i*i, "ends in 9")
print(count4, "numbers end in 4 when squared")
print(count9, "numbers end in 9 when squared")