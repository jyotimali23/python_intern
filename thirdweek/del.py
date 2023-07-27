class Employee:
	id=10
	name ="john"
	def display(self):
		print("id:%\nname %s"%(self.id,self.name))
emp=Employee()
emp.display()
print("obj is delet")