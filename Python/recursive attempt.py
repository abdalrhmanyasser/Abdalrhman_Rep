moves = []


def palindromcheck(n):
    if (n == reverse_numb(n)):
        print(moves)
        print("got it")
        moves.clear()
    else:
        nextnum(n)


def nextnum(n):
    moves.append([str(n) + " + " + str(reverse_numb(n)), n + reverse_numb(n)])
    palindromcheck(n + reverse_numb(n))


def reverse_numb(st):
    sr = str(st)
    return int(sr[::-1])


inp = input("type a number: \n")
while True:
    if (inp.isnumeric()):
        nextnum(int(inp))
        inp = 'sda'
    else:
        inp = input("type a real number: \n")
