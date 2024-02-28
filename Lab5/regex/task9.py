import re

s = input()

x = re.sub(r"(\w)([A-Z])", r"\1 \2", s)
print(x)
