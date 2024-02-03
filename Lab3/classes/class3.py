class Shape:
    area = 0

    def printArea(self): #prints area of a shape
        print(self.area)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def computeArea(self): #finds area of a rectangle
        self.area = self.length * self.width


a = Shape()
c = Rectangle(5, 2)

a.printArea()
print(c.length, c.width)
c.computeArea()
c.printArea()
