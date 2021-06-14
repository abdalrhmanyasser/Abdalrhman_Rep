from random import *
l = []
for i in range(50):
    l.append(randint(1, 100))
sumsOfNums = 0
for i in l:
    if i > 50:
        sumsOfNums += 1

print(l, "\nand", sumsOfNums, "numbers above 50")