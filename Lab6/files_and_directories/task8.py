import os

path = input()

if os.path.exists(path):
    os.remove(path)
else:
    print("The file does not exist.")