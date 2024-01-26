#ex1

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #output: banana


#ex2

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #output: cherry


#ex3

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #output: ['cherry', 'orange', 'kiwi']


#ex4

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #output: ['apple', 'banana', 'cherry', 'orange']


#ex5

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']


#ex6

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #output: ['orange', 'kiwi', 'melon']


#ex7

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")