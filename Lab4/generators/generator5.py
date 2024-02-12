def numbers(N):
    while N >= 0:
        yield N
        N -= 1

gen = numbers(25)

for i in gen:
    print(i)