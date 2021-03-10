temp = int(input("temp in C"))
if temp<-273.15:
    print("Invalid!")
elif temp == -273.15:
    print("temp is absoulute 0")
elif temp == 0:
    print("temp is at freezing point")
elif 0<temp<100:
    print("temp is in normal range")
elif temp==100:
    print("temp is at boiling point")
elif temp>100:
    print("temp is abovew boiling point")