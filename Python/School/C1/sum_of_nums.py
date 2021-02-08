def printbox(inlist, size, lines, key):
    print(key*(size+2))
    for i in inlist:
        sum = key + i
        if (size+2)-2-len(i) < 0:
            raise AssertionError("The Size is lower than this element of the list " + i)
        for i in range((size+2)-2-len(i)):
            sum+=" "
        sum+=key
        print(sum)
    for i in range(lines-len(inlist)):
        print(key, " "*(size-1) + key)
    print(key*(size+2))

try:
    file = open("text.txt", "rt")
except:
    file = open("text.txt", "x")
    file.close()
    file = open("text.txt", "rt")
text = file.readlines()
for i in range(len(text)):
    if "\n" in text[i]:
        text[i] = text[i].split("\n")
        text[i].pop()
        text[i] = "".join(text[i])
printbox(text, 20, 20, "*")