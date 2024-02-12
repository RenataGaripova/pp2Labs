def between_3_and_4(N):
    for i in range(N + 1):
        if (i % 3 == 0 and i % 4 == 0):
            yield i

n = int(input())

gen = between_3_and_4(n)

print(type(gen))

for i in gen:
    print(i)
