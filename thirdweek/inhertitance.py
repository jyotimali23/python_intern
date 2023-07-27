class A:
	def a(self,r):
		self.rollno
		print("parentclass")
		
class B(A):
	def b(self):
		print("class b")
class C(B):
	def c(self):
		print("class c")
class D(A):
	def d(self):
		print("class d")
obj=D()
obj.a()
obj.d()
