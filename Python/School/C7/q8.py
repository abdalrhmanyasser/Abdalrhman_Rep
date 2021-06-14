L = eval(input("the first list : "))
M = eval(input("the second list : "))
new = []
if len(L) == len(M):
    for i in range(len(M)):
        new.append(L[i] + M[i])
print(new)