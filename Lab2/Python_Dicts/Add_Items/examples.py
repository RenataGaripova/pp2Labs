#ex1

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict) #output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


#ex2

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"}) #output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}