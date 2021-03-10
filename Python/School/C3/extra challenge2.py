size = int(input("what is the hight you want"))
# this is added so that size of the letter looks correct
size*=2
def PrintLetterA(width):
    # this if statment is so that its compatible with both odd and even numbers
    if width/2 % 2 == 0:
        # we print the top star then print the top section of the A
        print(" "*((width//2) + 1) + "*")
        for i in range(1, (width//4)):
            print(" "*((width//2) - i + 1) + "*" + " "*(i*2-1) + "*")
    else:
        # we print the top star then print the top section of the A
        print(" "*((width//2)) + "*")
        for i in range(1, (width//4)):
            print(" "*((width//2) - i) + "*" + " "*(i*2-1) + "*")
    # we print the line going through the A
    print(" "*((width//4)+1) + "*"*(i*2+3))
    # we print the last part of A
    for i in range(1, (width//4)):
        print(" "*((width//4) - i + 1) + "*" + " "*(((width//4)*2)+i+i - 1) + "*")
# calling the function
PrintLetterA(size)
# Made by Abdalrhman Yasser Grade 10B