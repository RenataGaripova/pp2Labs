#ex1

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #output: ['apple', 'banana', 'cherry', 'orange']


#ex2

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) #output: ['apple', 'orange', 'banana', 'cherry']


#ex3

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


#ex4

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']