#ex1

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
#prints all keys


#ex2

for x in thisdict:
  print(thisdict[x])
#prints all values


#ex3

for x in thisdict.values():
  print(x)
#prints all values


#ex4

for x in thisdict.keys():
  print(x)
#prints all keys


#ex5

for x, y in thisdict.items():
  print(x, y)
#loop through both keys and values, by using the items() method: