from abc import ABC,abstractmethod

class poly(ABC):
	@abstractmethd
	def sides(self):
		pass
class Traingle(poly):
 	def sides1(slef):
 		print("traingle has 3 sides")
 	def sides(self):
 		print("poly method")
class Pentoge(poly):
	def sides(self):
		print("Pentoge has 5 sides")
class Hexagone(poly):
	def sides(self):
		print("Hexagone has 6 sideds")
p=Traingle()
p.sides()
p.sides1()
