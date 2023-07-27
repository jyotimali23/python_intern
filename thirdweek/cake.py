class Cake:
	def __init__(self,flavor,price):
		self.flover=flavor
		self.price=price
	def bake(self):
		print(f"a{self.flover} cake is being baked")
	def decorate(self):
		print("the cake is being decoarte")
	def dispaly(self):
		print(f"flover:{self.flover}")
		print(f"price:{self.price}")
chocalte = Cake("choclate",20)
chocalte.bake()
chocalte.decorate()
chocalte.dispaly()

