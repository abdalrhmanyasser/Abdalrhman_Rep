s = input()
a = s.split(" ")
for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if ord(a[j][-1].lower()) < ord(a[j+1][-1].lower()):
            Temp = a[j]
            a[j] = a[j+1]
            a[j+1] = Temp
print(" ".join(a))