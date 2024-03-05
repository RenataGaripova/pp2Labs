import os

path = input()

if os.access(path, os.F_OK):
    print("The path exists.")
else:
    print("The path does not exist.")

if os.access(path, os.R_OK):
    print("The path is readeble.")
else:
    print("The path is not readeble.")

if os.access(path, os.W_OK):
    print("The path is writable.")
else:
    print("The path is not writable.")

if os.access(path, os.X_OK):
    print("The path is executable.")
else:
    print("The path is not executable.")
