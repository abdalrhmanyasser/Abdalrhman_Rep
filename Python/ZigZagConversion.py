s = "PAYPALISHIRING"
x = []
numRows = int(input())
inbetweens = False
currentRowNum = 0
for i in range(numRows):
    x.append([])
for i in range(len(s)):
    if inbetweens:
        x[currentRowNum].append(s[i])
        currentRowNum-=1
        if currentRowNum<=0:
            inbetweens=False
    else:
        x[currentRowNum].append(s[i])
        print(currentRowNum, numRows)
        if numRows != 1:
            currentRowNum+=1
        if currentRowNum>=numRows-1:
            inbetweens=True
            
FinalString = ""
for i in x:
    FinalString += "".join(i)
print(FinalString)