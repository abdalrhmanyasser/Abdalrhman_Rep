from random import *
l = []
for i in range(20):
    l.append(randint(1, 12))
print(l)
for i in range(len(l)):
    if l[i] > 10:
        l[i] = 10
print(l)