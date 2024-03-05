F = open("demo4.txt", "r")

line_num = 0

for line in F:
    line_num += 1

print(f"The number of lines in the file is {line_num}.")

F.close()