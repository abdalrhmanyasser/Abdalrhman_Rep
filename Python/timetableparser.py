from datetime import datetime
c_path = "D:\\timetable conv type.txt"
final_var = []
try:
    file = open(c_path, "rt")
except:
    file = open(c_path, "x")
    file.close()
    file = open(c_path, "rt")
thing = file.readlines()

for i in range(5):
    thing[i] = thing[i].replace("\n", "", -1).split(" ")
print("thingy : ",thing)