from random import *
l=[]
divisable = []
for i in range(20):
    l.append(randint(1, 10))
    if i != 0:
        if l[i] % i == 0:
            divisable.append("YES")
        else:
            divisable.append("NO")
print(l, divisable, sep="\n")
