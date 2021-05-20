count = 0
for i in range(101):
    if (i*i) % 10 == 1:
        count+=1
        print(i, "with a square : ", i*i)
print(count, "numbers end in 1 when squared")