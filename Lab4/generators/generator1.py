def squares_to_N(N):
    for i in range(N + 1):
        yield i ** 2

#other way

n = int(input())
gen_squares = (i ** 2 for i in range(n))
