from math import *

n = int(input("Enter the number of sides.\n"))
a = int(input("Enter the length of a side.\n"))

angle = radians(180 // n) #angle to radians
cot = 1 / tan(angle) #cotangent of the angle

S = ((n * a ** 2) / 4) * cot #area of a polygon

print(round(S, 2))