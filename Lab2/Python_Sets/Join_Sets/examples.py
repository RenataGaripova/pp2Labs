#ex1

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) #output: {2, 1, 'b', 'c', 3, 'a'}


#ex2

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) #output: {'c', 3, 'a', 1, 'b', 2}


#ex3

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x) #output: {'apple'}


#ex4

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z) #output: {apple}


#ex5

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x) #output: {'google', 'banana', 'microsoft', 'cherry'}


#ex6

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z) #output: {'google', 'banana', 'microsoft', 'cherry'}


#ex7

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)
print(z) #output: {2, 'google', 'cherry', 'banana'}