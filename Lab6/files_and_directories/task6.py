import os, string

alph = string.ascii_uppercase

for letter in alph:
    filename = "letter_files\\" + letter + ".txt"
    if not os.access(filename, os.F_OK):
        F = open(filename, "w")
        result = f"The {filename} was created."
        F.write(result)
        F.close()