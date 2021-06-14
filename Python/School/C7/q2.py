from random import *
l = []
for i in range(50):
    l.append(randint(1, 100))
print(l)
for i in range(len(l)):
    l[i] **= 2
print(l)