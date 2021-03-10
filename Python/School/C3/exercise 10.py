from math import cos, sin, tan, pi, radians
print("Angle\tSine\t\t\t\tCosine")
for i in range(0, 361, 15):
    print(str(i) + "\t" + format(sin(radians(i)), ".20f").zfill(23) + "\t\t" + format(cos(radians(i)), ".20f").zfill(23))