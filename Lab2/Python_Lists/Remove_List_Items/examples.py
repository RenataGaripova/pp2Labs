#ex1

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #output: ['apple', 'cherry']


#ex2

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #output: ['apple', 'cherry', 'banana', 'kiwi']


#ex3

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #output: ['apple', 'cherry']


#ex4

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #['apple', 'banana'


#ex5

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #output: ['banana', 'cherry']


#ex6

thislist = ["apple", "banana", "cherry"]
del thislist #deleting the list completely


#ex7

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #output: []
