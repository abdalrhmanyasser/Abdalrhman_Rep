for n in range(2000):
    sums = 0
    for i in range(1, n):
        if n%i == 0:
            sums += i
    if sums == n and n != 0:
        print(sums)