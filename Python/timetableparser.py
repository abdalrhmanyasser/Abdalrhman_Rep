from datetime import datetime
c_path = "C:\\Users\\abdal\\Desktop\\timetable conv type.txt"
final_var = []
try:
    file = open(c_path, "rt")
except:
    file = open(c_path, "x")
    file.close()
    file = open(c_path, "rt")
thing = file.readlines()

for i in range(7):
    thing[i] = thing[i].replace("\n", "", -1).split(" ")
print(thing)
for _ in range(5):
    final_var.append([])
for j in range(5):
    print(thing)
    for i in range(7):
        final_var[j].append(thing[i][j])
print(final_var)