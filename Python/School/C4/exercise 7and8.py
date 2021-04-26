import random
try:
    file = open("results.re", "r")
except:
    file = open("results.re", "x")
    file.close()
    file = open("results.re", "r")
if file.read() == "":
    file.close()
    file = open("results.re", "w")
else:
    file.close()
    raise FileExistsError("""the exam was already taken, you cannot take the exam twice
    if the exam turned off on it own, that means you did two attempts at cheating""")
file = open("results.re", "a")
questions = []
operators = ["*", "+", "-"]
low = int(input("lowest num you want"))
high = int(input("highest num you want"))
num_of_questions = int(input("how many Questions do you want "))
wrong_questions = 0
correct_questions = 0
for i in range(num_of_questions):
    questions.append(str(random.randint(low, high)) + operators[random.randint(0,2)] + str(random.randint(low, high)))
answers = []
for i in range(len(questions)):
    answers.append(eval(questions[i]))
for i in range(len(questions)):
    question_index = random.randint(0, len(questions) - 1)
    random_question = questions[question_index]
    random_answer = answers[question_index]
    questions.remove(random_question)
    answers.remove(random_answer)
    user_answer = input("Question " + str(i+1) + " : " + random_question+ " = ")
    try:
        if int(user_answer) == random_answer:
            print("Correct")
            correct_questions+=1
            file.write("question " + str(i+1) + " user answered : " + user_answer + " Correct\t real answer : " + str(random_answer) + "\n")
        else:
            print("Wrong!")
            file.write("question " + str(i+1) + " user answered : " + user_answer + " Wrong\t\t real answer : " + str(random_answer) + "\n")
            file.write("question " + str(i+1) + " second try")
            print(user_answer, random_answer, int(user_answer) - random_answer)
            if -2 < int(user_answer) - random_answer < 2:
                print("Try Again! :)")
                user_answer = input("Question " + str(i+1) + " : " + random_question+ " = ")
                if int(user_answer) == random_answer:
                    print("Correct")
                    correct_questions+=.5
                    wrong_questions+=.5
                    file.write("question " + str(i+1) + " user answered : " + user_answer + " Correct\t real answer : " + str(random_answer) + "\n")
                else:
                    print("Wrong!")
                    wrong_questions+=1
                    file.write("question " + str(i+1) + " user answered : " + user_answer + " Wrong\t\t real answer : " + str(random_answer) + "\n")
            else:
                wrong_questions+=1
    except:
        print("please write the correct syntax")
        print("if you fail to comply the test will be regarded as a zero")
        user_answer = input("Question " + str(i+1) + " : " + random_question+ " = ")
        try:
            if int(user_answer) == random_answer:
                print("Correct")
                correct_questions+=1
            else:
                print("Wrong!")
                wrong_questions+=1
        except:
            file.write("Exam was cheated on" + "\n")
            file.write("wrong answers : all\tPercentage : 100%" + "\n")
            raise FileExistsError("""the exam was already taken, you cannot take the exam twice
    if the exam turned off on it own, that means you did two attempts at cheating""")
print("correct answers :", str(correct_questions) + "\tPercentage:", str((correct_questions / num_of_questions)*100) + "%")
print("wrong answers :", str(wrong_questions) + "\tPercentage:", str((wrong_questions / num_of_questions)*100) + "%")
file.write("correct answers : "+ str(correct_questions) + "\tPercentage: "+ str((correct_questions / num_of_questions)*100) + "%")
file.write("wrong answers : " + str(wrong_questions) + "\tPercentage: " + str((wrong_questions / num_of_questions)*100) + "%")
