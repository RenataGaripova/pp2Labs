import re

s = input()

x = re.search('ab*', s)

print(x)