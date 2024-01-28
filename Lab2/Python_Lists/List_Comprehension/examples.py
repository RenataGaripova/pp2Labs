#ex1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) #output: ['apple', 'banana', 'mango']


#ex2

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) #output: ['apple', 'banana', 'mango']


#ex3

#syntax - newlist = [expression for item in iterable if condition == True]


#ex4

newlist = [x for x in fruits if x != "apple"] #['banana', 'cherry', 'kiwi', 'mango']

#ex5

newlist = [x for x in fruits]


#ex6

newlist = [x for x in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#ex7

newlist = [x for x in range(10) if x < 5] #[0, 1, 2, 3, 4]


#ex8

newlist = [x.upper() for x in fruits] #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


#ex9

newlist = ['hello' for x in fruits]


#ex10

newlist = [x if x != "banana" else "orange" for x in fruits]

