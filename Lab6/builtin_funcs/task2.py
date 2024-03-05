S = input()

Upper = 0
Lower = 0

for i in S:
    if 65 <= ord(i) <= 90:
        Upper += 1
    elif 97 <= ord(i) <= 122:
        Lower += 1

print(f"Upper case: {Upper}, Lower case: {Lower}")

