from random import *
Moves = []
Final = []
Moves.append("R")
Moves.append("U")
Moves.append("D")
Moves.append("F")
Moves.append("L")
Moves.append("B")
for x in range(randrange(20, 30)):
    y = randrange(6)
    Final.append(Moves[y])
    # TODO: write code...
c = len(Final)
a = -c
print(len(Final))
print(Final)
for z in range(c):
    print(" ")
    if z != c+1:
      if c -z > 2:
        if Final[z] == Final[z + 1] and Final[z + 1] == Final[z + 2]:
            Final[z] = Final[z] + "'"
            Final.pop(z + 1)
            Final.pop(z + 1)
            a += 1
            c -= 2
            print(Final)
        elif random() < .1:
          Final[z] = Final[z] + "'"
        elif random() < .2:
          Final[z] = Final[z] + "2"
      if c - z > 1:
        if Final[z] == Final[z + 1]:
          Final[z] = Final[z] + "2"
          Final.pop(z + 1)
          c -= 1
          print(Final)
        elif Final[z+1] in Final[z]:
          Final.pop(z+1)
          Final.pop(z)
          a += 1
          c -= 2
    a += 1
print(Final)
print(" ")
print(" ")
print(" ")