#ex1

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) #output: {'cherry', 'orange', 'apple', 'banana'}


#ex2

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) #output: {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}


#ex3

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) #output: {'banana', 'cherry', 'apple', 'orange', 'kiwi'}

