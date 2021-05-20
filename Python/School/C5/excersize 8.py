arrOfMarks=[]

for i in range(10):
    Input = eval(input("enter the num"))
    arrOfMarks.append(Input)

for i in arrOfMarks:
    if i > 100:
        print("one of the marks is higher than 100")
        exit()
print("the highest mark :", max(arrOfMarks))
print("the lowest mark :", min(arrOfMarks))