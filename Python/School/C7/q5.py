from random import *
l = []
for i in range(200):
    l.append(randint(1, 100))
print(l)
l2 = []
for i in range(100):
    l2.append(l.count(i))
print(l2)