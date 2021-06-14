# Question 9: Write a program that asks the user for an integer and creates a list that consists of the factors
# (divisors) of that integer.

num = int(input("enter a number"))
L = []
for i in range(num):
    if i %num ==0:
        L.append(i)
print(L)