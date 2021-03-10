num = eval(input("enter a number : "))
sum = 0
for i in range(0, num + 1):
    sum += i*i
print("the sum of the squars from 0 to and", num, "is", sum)