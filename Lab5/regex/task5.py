import re

s = input()

x = re.search('a.*b', s)

print(x)