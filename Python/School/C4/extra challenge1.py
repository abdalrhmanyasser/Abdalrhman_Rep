upper = int(input("Enter the num"))
print("primes under", upper)
for num in range(upper):
    if num > 1: 
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num,"is a prime number")