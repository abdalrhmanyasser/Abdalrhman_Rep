from random import *
L1 = []
L2 = []
L3 = []
for i in range(10):
    L1.append(randint(1, 11))
    L2.append(randint(10, 21))
print("L1 : " + str(L1),"L2 : " + str(L2), sep="\n")
for i in range(len(L1)):
    if L1[i] % 2 == 1:
        L3.append(L1[i])
    if L2[i] % 2 == 0:
        L3.append(L2[i])
L3.sort()
print("L3 : " + str(L3))
