num = int(input("Enter the num"))
sum = 1
i = 2
while i * i <= num:
    if num % i == 0:
        sum = sum + i + num/i
    i += 1

if sum == num and num!= 1:
    print(num, "is a perfect number")