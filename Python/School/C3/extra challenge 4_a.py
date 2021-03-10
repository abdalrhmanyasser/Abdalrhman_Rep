# Part A
a = int(input("enter first num : "))
print("the first digit of", a**a, "is :",a**a%10)
# Part B
b = int(input("enter first num : "))
print("the first two digit of", b**b, "are :",b**b%100)
# Part C
power = int(input("Enter the Power : "))
digits = int(input("Enter the number of digits you want : "))
print("the first", digits, "digits of", 2**power, "are :",(2**power)%(10**digits))
