#ex1

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#ex2

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#ex3

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#ex4

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)