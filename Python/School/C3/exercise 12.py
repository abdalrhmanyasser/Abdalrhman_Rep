# getting inputs
width = int(input("width = "))
height = int(input("height = "))
# repeats will keep track of length of rows
repeats = 0
# main loop
for i in range(width*height):
    repeats += 1
    print(i%10, end=" ")
    if (repeats == width):
        print("")
        repeats = 0