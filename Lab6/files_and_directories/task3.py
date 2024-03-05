import os

path = input()

if os.access(path, os.F_OK):
    print("Path exists.")

    filename = os.path.basename(path)

    print(f"Name of the file is {filename}")

    dirname = path.replace(filename, '')

    print(f"Name of the directory is {dirname[:-1]}")

else:
    print("Path does not exist.")