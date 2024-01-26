#ex1

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) #output: apple
           #banana
           #cherry

#ex2

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) #output: apple
                     #banana
                     #cherry


#ex3

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#ex4

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]