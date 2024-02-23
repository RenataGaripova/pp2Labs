import re

s = input()

x = re.search('[a-z]+_{1}[a-z]+', s)

print(x)