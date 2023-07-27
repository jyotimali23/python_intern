class Recantangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        print(self.l*self.w)
    def perimeter(self):
        print(2*self.l+2*self.w)
class Square:
    def __init__(self,l):
        self.l=l
    def area(self):
        print(self.l*self.l)
    def perimeter(self):
        print(4*self.l)
obj=Recantangle(2,3)
obj.area()
obj.perimeter()
obj1=Square(4)
obj1.area()
obj1.perimeter()