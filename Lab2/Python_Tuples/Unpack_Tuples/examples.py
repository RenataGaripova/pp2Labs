#ex1

fruits = ("apple", "banana", "cherry") #packing a tuple'


#ex2

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green) #output: apple
print(yellow) #output: banana
print(red) #output: cherry


#ex3

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) #output: apple
print(yellow) #output: banana
print(red) #output: ['cherry', 'strawberry', 'raspberry']


#ex4

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green) #output: apple
print(tropic) #output: ['mango', 'papaya', 'pineapple']
print(red) #output: cherry