from math import sqrt

def squares(a, b):
    for i in range(a, b + 1):
        if int(sqrt(i)) == sqrt(i):
            yield i


A, B = map(int, input().split())
gen = squares(A, B)

for i in gen:
    print(i)
