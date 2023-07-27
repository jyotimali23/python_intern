class Recantangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        print(self.l*self.w)
    def perimeter(self):
        print(2*self.l+2*self.w)
class Square(Recantangle):
    def __init__(self,l):
        super().__init__(l,l)
    # def area1(self):
    #     print(self.l*self.l)
    # def perimeter1(self):
    #     print(4*self.l)
obj1=Square(2)
obj1.area()
obj1.perimeter() 