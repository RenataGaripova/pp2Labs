#ex1

myset = {"apple", "banana", "cherry"}


#ex2

thisset = {"apple", "banana", "cherry"}
print(thisset)


#ex3

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #output: {'banana', 'cherry', 'apple'}


#ex4

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) #output: {True, 2, 'banana', 'cherry', 'apple'}


#ex5

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset) #output: {False, True, 'cherry', 'apple', 'banana'}