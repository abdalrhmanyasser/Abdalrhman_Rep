from math import cos, sin, tan, pi, radians
print("Angle Sine Cosine")
for i in range(0, 361, 1):
    print(str(i) + " " + format(sin(radians(i)), ".20f").zfill(23) + " " + format(cos(radians(i)), ".20f").zfill(23))