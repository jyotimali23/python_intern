class BakeryIteam:
	def __init__(self,name,price):
		self._name=name		
		self._price=price

	def get_name(self):
		return self._name
	def set_price(self,price):
		if price>=0:
			self._price=price
		else:
			print("invalid price")
	def display_info(self):
		print(self._name)		
		print(self._price)
iteam=BakeryIteam("choclatecake",0)
print(iteam.get_name())
iteam.set_price(0)
iteam.display_info()

