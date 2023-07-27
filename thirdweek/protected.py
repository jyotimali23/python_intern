class Student:
    _schoolName = 'XYZ School' 
    def __init__(self, name, age):
        self._name= name
        self._age=age 
std = Student("Swati", 25)
print(std._name)  

std._name = 'Dipa'
print(std._name)  

