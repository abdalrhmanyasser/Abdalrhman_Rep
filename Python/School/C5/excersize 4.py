sums = 0
for i in range(2001):
    if i%2==0:
        sums -= i
    else:
        sums += i
print(sums)