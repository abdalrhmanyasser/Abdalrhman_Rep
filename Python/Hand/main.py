players = []
playerScores = []
playerNum = int(input("input number of player : "))

for i in range(playerNum):
    print("enter the name of player #", i+1)
    players.append(input("Name : "))
    playerScores.append(int(input("Enter " + players[i] + "'s Score : ")))
while True:
    menu = "Enter the winning type :\n\t1. 100\n\t2. 200\n\t3. 1000\n\t4. 2000\n\t5. 3000\n\t6. 4000\n\t7. did someone cheat or havve a wrong hand\n"

    print("Players: ")
    for i in range(playerNum):
        print(str(i+1) + ". " + players[i], " : ", playerScores[i])
        
    winningStates = [100, 200, 1000, 2000, 3000, 4000]
    winningBonus = {100:30, 200:60, 1000:150, 2000:300, 3000:450, 4000:600}

    winningType = int(input(menu))


    if winningType == 7:
        print("Who is the dumb idiot : ")
        dumbIdiot = input("Name : ")
        playerScores[players.index(dumbIdiot)] -= 50
    else:
        whoWon = players[int(input("Enter who won (index) : "))-1]
        ans = input("Did " + whoWon + " pick the last card from the person before (Y/y for yes): ")
        LastCardPicked = (ans == 'y' or ans == 'Y')
        if LastCardPicked:
            playerScores[(players.index(whoWon)-1 if players.index(whoWon)-1 >= 0 else playerNum-1)] += 50

        luckyPieceOfShit = []
        print("Enter names of who put cards down (91s) (Names) : ")
        name = "."

        num = 1
        name = input(str(num) + ". ")
        while name != "":
            luckyPieceOfShit.append(name)
            num+=1
            name = input(str(num) + ". ")
        print("input the card counts for the following players : ")
        left = list(range(playerNum))
        for i in range(len(luckyPieceOfShit)):
            playerScores[players.index(luckyPieceOfShit[i])] += (int(input(luckyPieceOfShit[i] + ". ")) * winningType)
            left.pop(players.index(luckyPieceOfShit[i]))
        left.pop(players.index(whoWon))
        for j in left:
            playerScores[j]+=winningStates[winningType-1]
            
        playerScores[players.index(whoWon)] -= winningBonus[winningStates[winningType-1]]


            
            