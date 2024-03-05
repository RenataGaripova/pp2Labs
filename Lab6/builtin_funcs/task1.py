lst = [8, 2, 3, 'a', 'b', 1, '?']

res = 1

for i in lst:
    if isinstance(i, int):
        res *= i

print(res)