from math import *
sums = 0
for n in range(1, eval(input("Write N\n")) + 1):
    sums += 1/n
sums -= log(n)
print(sums)