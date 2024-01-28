#ex1

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) #output: ("apple", "kiwi", "cherry")


#ex2

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) #('apple', 'banana', 'cherry', 'orange')


#ex3

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) #output: ('apple', 'banana', 'cherry', 'orange')


#ex4

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y) #('banana', 'cherry')


#ex5

thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) this will raise an error because the tuple no longer exists