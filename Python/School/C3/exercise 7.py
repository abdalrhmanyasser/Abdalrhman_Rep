present = int(input('Enter time : '))
hrsInFuture = int(input('How many hours ahead ? '))
if (present + hrsInFuture > 12):
    thingy = "PM"
else :
    thingy = "AM"
print("new hour :", (present + hrsInFuture) % 12, thingy)