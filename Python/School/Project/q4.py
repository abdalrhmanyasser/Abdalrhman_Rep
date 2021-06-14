from random import *
l=[]
for i in range(101):
    l.append(randint(0, 1))
print(str(l.count(0))+" of 0\n" + str(l.count(1))+" of 1")
