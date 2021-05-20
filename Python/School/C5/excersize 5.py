sums = 0
n = eval(input("enter a number"))
for i in range(1, n):
    if n%i == 0:
        sums += i
print(sums)