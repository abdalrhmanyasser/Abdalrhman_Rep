from pip._vendor.colorama import init
init()
class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'
ending_string = bg.WHITE + " " + style.RESET_ALL
generation = 0
intialarr = [
    ['X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'X'],
    ['O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
    ['X']*40,
    ['X']*40,
    ['X']*40,
    ['X']*40,
    ['X']*40,
    ['X']*40,
    ['X']*40,
    ['X']*40,
    ['X']*40,
    ['X']*40,
    ['X']*40,
    ['X']*40,
    ['X']*40,
    ]
arrnabrs = []
for i in range(len(intialarr)):
    arrnabrs.append([])
    for j in range(len(intialarr[i])):
        arrnabrs[i].append(0)

def drawgrid(array):
    for row in array:
        print("\n" + bg.WHITE + ' '*(75*2+11) + style.RESET_ALL)
        print(bg.WHITE, style.RESET_ALL, end="")
        for col in row:
            if col == 'O':
                print(bg.GREEN, 'O', style.RESET_ALL, end=ending_string)
            else:
                print(bg.BLUE, 'X', style.RESET_ALL, end=ending_string)
    print("\n" + bg.WHITE + ' '*(75*2+10) + style.RESET_ALL)
loop = True
drawgrid(intialarr)
arr = list(map(list, intialarr))
gen_progress = input("how many genartation do you want to skip each time\n")
while loop:
    inp = input("\ncontinue\n")
    if inp.lower() == "e":
        loop = False
        break
    else:
        for i in range(int(gen_progress)):
            parr = list(map(list, arr))
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    nabours = 0
                    Top = not (i == 0)
                    Bottom = not (i == len(arr) -1)
                    Left = not (j == 0)
                    Right = not (j == len(arr[i]) -1)
                    if (Top):
                        if parr[i-1][j] == 'O':
                            nabours+=1
                    if (Bottom):
                        if parr[i+1][j] == 'O':
                            nabours+=1
                    if (Left):
                        if parr[i][j-1] == 'O':
                            nabours+=1
                    if (Right):
                        if parr[i][j+1] == 'O':
                            nabours+=1
                    if(Top and Left):
                        if parr[i-1][j-1] == 'O':
                            nabours+=1
                    if(Bottom and Right):
                        if parr[i+1][j+1] == 'O':
                            nabours+=1
                    if(Top and Right):
                        if parr[i-1][j+1] == 'O':
                            nabours+=1
                    if(Bottom and Left):
                        if parr[i+1][j-1] == 'O':
                            nabours+=1
                    arrnabrs[i][j] = nabours

            for x in range(len(arr)):
                for y in range(len(arr[x])):
                    if arrnabrs[x][y] > 3 and parr[x][y] == 'O':
                        arr[x][y] = 'X'
                    elif arrnabrs[x][y] == 2 and parr[x][y] =='O':
                        arr[x][y] = 'O'
                    elif arrnabrs[x][y] == 3:
                        arr[x][y] = 'O'
                    elif arrnabrs[x][y] < 3 and parr[x][y] == 'O':
                        arr[x][y] = 'X'
    drawgrid(arr)
