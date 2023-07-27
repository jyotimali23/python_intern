from abc import ABCMeta, abstractmethod
class Shape:
    __metaclass__ = ABCMeta 
    def __init__ (self, shapeType):
        self.shapeType = shapeType
    @abstractmethod 
    def area(self) :
        pass
    @abstractmethod
    def perimeter (self):
        pass
class Rectangle(Shape):
    def __init__(self, length, breadth):
        Shape.__init__(self, Rectangle)
        self.length = length
        self.breadth = breadth
    def area (self):
        print("rec area",self.length * self.breadth)
    def perimeter (self):
        print("rec perimeter",2 * (self.length + self.breadth))
class Circle (Shape):
    pi = 3.14
    def __init__ (self, radius):
        Shape.__init__(self, Circle)
        self.radius = radius
    def area (self):
        print("circle area",round(Circle.pi * (self.radius ** 2), 2))
    def perimeter(self):
        print( "circle perimeter",round (2 * Circle.pi * self.radius, 2))
rectangle = Rectangle (30, 15)
rectangle.area ()
rectangle.perimeter ()
circle = Circle (5)
circle.area ()
circle.perimeter()
print(f"circle class is {Circle.__class__}/n")
print(f"rectanle class's class is {Shape.__class__.__class__}/n")
print(f"shape class is {rectangle.__class__.__class__.__class__}")
