from random import *
l = []
for i in range(50):
    l.append(randint(1, 100))
print(l)
l.sort()
print(l[0], l[1])
print(l[-2], l[-1])