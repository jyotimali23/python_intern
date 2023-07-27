class Area:
	def __init__(self,radius):
		self.radius = radius
	def display_info(self):
		print("area",self.radius)
class Prameter(Area):
	def __init__(self ,square):
		super().__init__(4)
		self.square = square
	def display_info(self):
		super().display_info()
		print("square",self.square)
obj1=Prameter(6)
obj1.display_info()
def mul(x):
	x*=1
	return value*2
value =10
value = mul(value)
print(value)