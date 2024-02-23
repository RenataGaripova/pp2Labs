import re

s = input()

x = re.search('abbb?', s)

print(x)