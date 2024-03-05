F1 = open("copyfrom.txt", "r")
F2 = open("copyto.txt", "w")

for line in F1:
    F2.write(line)

F2.close()