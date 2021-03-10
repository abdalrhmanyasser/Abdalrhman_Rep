import math
Y = int(input("what is the year"))
C = math.floor(Y / 100)
m_part1 = math.floor((13 + 8 * C) / 25)
M = (15 - m_part1 + C - math.floor(C / 4)) % 30
N = (4 + C - math.floor(C / 4)) % 7
A = Y % 4
B = Y % 7
C = Y % 19
D = (19 * A + M) % 30
E = (2 * A + 4 * B + 6 * D + N) % 7
days = (22 + D + E)
if ((D == 29) and (E == 6)):
    print(str(Y)+"-April-19")
elif ((D == 28) and (E == 6) and (M==2 or M == 5 or M == 10 or M == 13 or M == 16 or M == 21 or M == 24 or M == 39)):
    print(str(Y)+"-April-18")
else:
    if (days > 31):
        print(str(Y)+"-April", (days - 31), sep="-")
    else:
        print(str(Y)+"-March", days, sep="-")
