data = []
while True:
    data1 = input()
    if data1 == "":
        break
    data.append(data1)
datanodupe = []
for x in data:
    if x in datanodupe:
        pass
    else:
        datanodupe.append(x)
print(len(data), len(datanodupe))