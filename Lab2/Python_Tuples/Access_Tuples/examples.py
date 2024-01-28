#ex1

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #output: 'banana'


#ex2

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #output: 'cherry'


#ex3

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #output: ('cherry', 'orange', 'kiwi')


#ex4

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #output: ('apple', 'banana', 'cherry', 'orange')


#ex5

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) #output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')


#ex6

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) #output: ('orange', 'kiwi', 'melon')


#ex7

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") #output: Yes, 'apple' is in the fruits tuple