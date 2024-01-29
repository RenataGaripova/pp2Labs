#ex1

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]


#ex2

x = thisdict.get("model")


#ex3

x = thisdict.keys() #dict_keys(['brand', 'model', 'year'])

#ex4

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #output: dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) #outtput: dict_keys(['brand', 'model', 'year', 'color'])
