import re

s = input()
lst = [i for i in s]
x = re.findall('_[a-z]', s)

for i in range(len(lst) - 1):
    temp = lst[i] + lst[i + 1]
    if temp in x:
        lst[i] = ''
        lst[i + 1] = lst[i + 1].upper()

s = ''.join(lst)

print(s)

