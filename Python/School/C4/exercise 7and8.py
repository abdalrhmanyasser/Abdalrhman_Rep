import random
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
print(questions, "\n", answers)
for i in range(len(questions)):
    question_index = random.randint(0, len(questions) - 1)
    random_question = questions[question_index]
    random_answer = answers[question_index]
    questions.remove(random_question)
    answers.remove(random_answer)
    user_answer = input("Question " + str(i+1) + " : " + random_question+ " = ")
    if int(user_answer) == random_answer:
        print("Correct")
        correct_questions+=1
    else:
        print("Wrong!")
        wrong_questions+=1
print("correct answers :", str(correct_questions) + "\t", "Percentage:", str((correct_questions / num_of_questions)*100) + "%")
print("wrong answers :", str(wrong_questions) + "\t", "Percentage:", str((wrong_questions / num_of_questions)*100) + "%")
