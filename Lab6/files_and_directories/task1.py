import os

path = input()
dirs = os.listdir(path)

#list only directories

for elem in dirs:
    if os.path.isdir(os.path.join(path, elem)):
        print("This is a directory:", os.path.join(path, elem))
        

#list files and directories
        
for elem in dirs:
    if os.path.isdir(os.path.join(path, elem)):
        print("This is a directory:", os.path.join(path, elem))
    if os.path.isfile(os.path.join(path, elem)):
        print("This is a file:", elem)

#list only files

for elem in dirs:
    if os.path.isfile(os.path.join(path, elem)):
        print("This is a file:", elem)