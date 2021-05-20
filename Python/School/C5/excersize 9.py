import random
changed = [0, 0]
unchanged = [0, 0]
for i in range(10000):
    arrOfChoices = [1, 2, 3]
    correct = random.choice(arrOfChoices)
    incorrect = arrOfChoices.copy()
    incorrect.remove(correct)
    userChoice = random.choice(arrOfChoices)
    arrOfChoices.remove(random.choice(incorrect))
    if random.randint(0, 1) > .5:
        if userChoice == correct:
            unchanged[1]+=1
        else:
            unchanged[0]+=1
    else:
        userChoice = random.choice(arrOfChoices)
        if userChoice == correct:
            changed[1]+=1
        else:
            changed[0]+=1
print("its better to change your answer after the reviel :", changed[1] > unchanged[1])
print(changed[1], unchanged[1], "its this", changed[1] / unchanged[1], "much better")