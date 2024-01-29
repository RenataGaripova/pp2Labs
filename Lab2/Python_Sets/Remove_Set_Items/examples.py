#ex1

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) #output: {'apple', 'cherry'}


#ex2

#discard does not raise an error if an object doesn't exist
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) #output: {'apple', 'cherry'}


#ex3
#pop removes random item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #output: banana
print(thisset) #output: {'apple', 'cherry'}


#ex4

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) #output: set()


#ex5

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists
