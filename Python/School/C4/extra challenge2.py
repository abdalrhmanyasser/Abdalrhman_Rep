print("primes under 100")
for num in range(100):
    if num > 1: 
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num,"is a prime number")
        
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num,"is not a prime number")