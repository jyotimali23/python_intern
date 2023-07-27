class Parent():
	def __init__(self):
		print("inside parent")
	def show1(self):
		print("geeks")
		
class Child(Parent):
	def __init__(self):
		#Parent.show1(self)
		#self.show1()
		Parent.__init__(self)
		print("Inside Child")
obj = Parent()
obj1 =Child()
obj1.show1()
