from math import sqrt

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self): #print point's coordinates
        print(self.x, self.y)

    def move(self, x2, y2): #changes point's coordinates
        self.x += x2
        self.y = y2

    def findDistance(self, other): #finds distance between 2 points
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


a = Point(0, 0)
b = Point(3, 4)

a.show()
b.show()

print(a.findDistance(b))

