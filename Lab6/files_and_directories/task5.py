F = open("demo5.txt", "w")

data = ["a", "b", "c", True, 3, 5, 6, 0, 1, "?"]

data = map(str, data)

F.write(" ".join(data))

F.close()

