import re

s = input()
x = re.findall('[A-Z]{1}', s)
s = ' '.join(x)

print(s)