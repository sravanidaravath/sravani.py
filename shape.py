class Shape:
    def area(self):
        print("Area of shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of Circle:", area)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print("Area of Rectangle:", area)

circle = Circle(5)
rectangle = Rectangle(8, 4)

circle.area()
rectangle.area()