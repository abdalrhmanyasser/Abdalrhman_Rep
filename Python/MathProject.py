d = input()
numbers = []
currentNum = 0

for i in range(len(d)):
    current = int(d[i])
    if (d[i].isdigit):
        if len(numbers) < currentNum+1:
            numbers.append(0)
        numbers[currentNum] = numbers[currentNum]*10 + int(d[i])
    elif d[i] in "+-*/%!^":
        if 