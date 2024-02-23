import re

s = input()

x = re.search('[A-Z]+[a-z]+', s)

print(x)
