from random import *
l=[]
new_l=[]
for i in range(10):
    l.append(randint(0, 25))
for i in range(len(l)):
    if not i==0 and not i==len(l)-1:
        new_l.append(l[i-1]+l[i]+l[i+1])
    elif i==0:
        new_l.append(l[i]+l[i+1])
    elif i==len(l)-1:
        new_l.append(l[i-1]+l[i])
print("l = "+str(l),"new_l = "+str(new_l),sep="\n")
