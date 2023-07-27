class Recantangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        (self.l*self.w)
    def perimeter(self):
        print(2*self.l+2*self.w)
class Square(Recantangle):
    def __init__(self,l):
        super().__init__(l,l)
class Cube(Square):
    def __init__(self):
        #f=super().area()
        f=Recantangle.area(self)
        print(f*6)
obj1=Cube(3)
obj1.surface()
#obj1.perimeter1() 