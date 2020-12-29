from random import randrange
from random import random
import time
import threading


print(" ")
print(" ")
#rounding for 2 decimal points#
def myMethod(n):
  return int(n * 100) / 100
#*****************************#

#Making the two Arrays that will hold our values#
  #MOVES will hold our possible scramble Moves#

Moves = []

#Our 6 total moves#
#M is not included because its useless#
Moves.append("R")
Moves.append("U")
Moves.append("D")
Moves.append("F")
Moves.append("L")
Moves.append("B")
#*************************************#

#calling the self-calling function#

def scrambling_Method():
  #FINAL will hold our result of our algorithem #
  Final = []
  #creating the random moves that will be simplified or improved#
  for x in range(randrange(20, 30)):
      y = randrange(6)
      Final.append(Moves[y])
  c = len(Final)
  a = -c

  #*************************************************************#

  #improvind the scramble#
  for z in range(c):
      if z != c+1:
        if c -z > 2:
          if Final[z] == Final[z + 1] and Final[z + 1] == Final[z + 2]:
              Final[z] = Final[z] + "'"
              Final.pop(z + 1)
              Final.pop(z + 1)
              a += 1
              c -= 2
          elif random() < .5:
            Final[z] = Final[z] + "'"
          elif random() < .3:
            Final[z] = Final[z] + "2"
        if c - z > 1:
          if Final[z] == Final[z + 1]:
            Final[z] = Final[z] + "2"
            Final.pop(z + 1)
            c -= 1
          elif Final[z+1] in Final[z]:
            Final.pop(z+1)
            Final.pop(z)
            a += 1
            c -= 2
          elif Final[z] in Final[z+1]:
            Final.pop(z+1)
            Final.pop(z)
            a += 1
            c -= 2
      a += 1
  print(Final)
  #**********************#


  #Waiting for the user to finish the scramble#
  print("press when finished the scramble")
  input()

  #This is for inspection time#
  for b in range(15):
    print("{0} until inspection finishes".format(15 -b))
    time.sleep(1)
  #***************************#
  #THE FULL TIMER#

  #Taking the starting time#

  start_time = time.time()

  #Taking the ending time#

  input("Press Enter to stop")
  end_time = time.time()

  #Calculating the min and sec from time passed#

  time_lapsed = end_time - start_time
  s = myMethod((time_lapsed) % 60)
  m = int((time_lapsed / 60))
  print(str(m) + " Mins " + str(s) + " Sec ")
  p = input("Do you want to play again y/n \n")
  if p in "y Y":
    scrambling_Method()
  
scrambling_Method()