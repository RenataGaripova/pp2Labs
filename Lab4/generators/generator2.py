def generate_evens(N):
    for i in range(0, N + 1, 2):
        yield i

n = int(input())
gen1 = generate_evens(n)

print(type(gen1))

print(*gen1, sep = ", ")

#other way

gen2 = (i for i in range(0, n + 1, 2))

print(type(gen2))

print(*gen2)
