class Recantangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        print(self.l*self.w)
    def perimeter(self):
        print(2*self.l+2*self.w)
obj=Recantangle(2,3)
obj.area()
obj.perimeter() 