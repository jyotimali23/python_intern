class BakeryIteam:
	def __init__(self,name,price):
		self._name=name
		self ._price =price
	def display_info(self):
		print("name",self._name)
		print("price",self._price)
	def sell(self):
		print("selling",self._name)
class Cake(BakeryIteam):
	def __init__(self,name,price,flavor):
		super().__init__(name,price)
		self._flavor=flavor
	def display_info(self):
		super().display_info()
		print("flavor",self._flavor)
	def decorate(self):
	    print("decorating",self._name)	
class Cookie(BakeryIteam):
	def __init__(self,name,price,shape):
		super().__init__(name,price)
		self._shape=shape
	def display_info(self):
			super().display_info()
			print("shape",self._shape)
	def pack(self):
		print("packing",self._name)
cake=Cake("choclatecake",25.0,"choclate")
cokkie=Cookie("choclatechipcokkie",30.0,"round")
Bakery_Iteam=[cake,cokkie]
cake.sell()
cake.decorate()
cokkie.pack()

for i in (Bakery_Iteam):
	i.display_info()
	i.sell()
