class Shape:

    def area(self): #prints area of a shape
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self): #prints area of a Square
        print(self.length ** 2)

a = Shape()
b = Square(7)

a.area()
b.area()