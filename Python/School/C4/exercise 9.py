import random
wins = 0
draws = 0
choices = ["rock", "Paper", "Siscors"]
for i in range(5):
    player_choice = input("r/p/s")
    if player_choice == "r":
        player = 1
    elif player_choice == "p":
        player = 2
    elif player_choice == "s":
        player = 3
    computer = random.randint(1, 3)
    if player - computer == 0:
        print("draw the opponent chose :", choices[computer - 1])
        draws+=1
    elif player - computer == -1:
        print("loss the opponent chose :", choices[computer - 1])
    elif player - computer == 2:
        print("loss the opponent chose :", choices[computer - 1])
    elif player - computer == 1:
        print("win the opponent chose :", choices[computer - 1])
        wins+=1
    elif player - computer == -2:
        print("win the opponent chose :", choices[computer - 1])
        wins+=1
print("you won :", wins, "wins out of 5")
print("you tied :", draws)