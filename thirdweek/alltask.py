#
# 2. You are building a simple messaging system. Create a class called Message. Now, create two subclasses of Message: 
# and SMS. Instantiate both subclasses and demonstrate how to use them to send different types of messages.
#:# 3. Create a Python class called BankAccount to represent a bank account
#Encapsulate the account holder's name, account number, and balance. 
# the BankAccount class and demonstrate how to set and retrieve these attributes.
# 4. Scena
# You are developing a Python applic…
#4
#from abc import ABCMeta, abstractmethod
# class Zoo: 
#     __metaclass__ = ABCMeta 
#     def __init__ (self, animalType):
#         self.animalType = animalType
#     @abstractmethod 
#     def speak(self) :
#         pass
#     @abstractmethod
#     def move (self):
#         pass
# class Dog (Zoo):
#     def __init__(self,type1,type2):
#         Zoo.__init__(self,Dog)
#         self.type1=type1
#         self.type2=type2
#     def speak (self):
#         print("dog is belogs to class and dog is speak ",self.type1)
#     def move (self):
#         print("dog move like ",self.type2)
# class Cat(Zoo:
#     def __init__(self, speak1,move1):
#         Zoo.__init__( self,Cat)
#         self.speak1=speak1
#         self.move1=move1
#     def speak (self):
#         print(f"cat is belogs to class and cat is  speak{self.speak1}")
#     def move (self):
#         print( " cat move like ",self.move1)
# d=Dog("barking","trottting")
# d.speak()
# d.move()
# c=Cat("meows","gait")
# c.speak()
# c.move()
#2polymorhism
class Message:
    def __init__(self,hello) :
        self.hello=hello
    def msg(self):
        print("Message type")
class Email(Message):
    def __init__(self, hello):
        super().__init__(hello)
        self.hello=hello
    def msg(self):
        print("emsil msg",self.hello)
class Sms(Message):
    def __init__(self, hello):
        super().__init__(hello)
        self.hello=hello
    def msg(self):
        print("sms message",self.hello)
e=Email("hii")
e.msg()
s=Sms("helllo")
s.msg()

 #1. You are building a simple employee management system. Create a class called Employee to 
#represent employees. Now, create a subclass Manager that inherits from the Employee class. Instantiate both
# classes and demonstrate how Manager inherits from Employee.
# class Empolyee:
#     def __init__(self,ename,esalary,eaddress):
#         self.ename=ename
#         self.esalary=esalary
#         self.eaddress=eaddress
# class Manager(Empolyee):
#     def __init__(self,ename,esalary,eaddress,mname,msalary,maddress):
#         super().__init__(ename,esalary,eaddress)
#         self.mname=mname
#         self.msalary=msalary
#         self.maddress=maddress
#     def dispaly(self):
#         print("Empolyee name is",self.ename)
#         print("Empolyee slary is",self.esalary)
#         print("Empolyee address is",self.eaddress)
#         print("Manager name is",self.mname)
#         print("Manager salary is",self.msalary)
#         print("Manager address is",self.maddress)

# m=Manager("varun",45000,"neemuch","ram",90000,"indore")
# m.dispaly()
class Bankaccount:
    def __init__(self,accountholder,balance,ac):
        self._accountholder=accountholder
        self._balance=balance
        self._ac=ac

    def get_name(self,accountholder,balance,ac):
        return self._accountholder,self._balance,self._ac
    def set_price(self,balance):
        if balance>=0:
            self._balance=balance
        else:
            print("invalid balane")
    def display_info(self):
        print(self._accountholder)       
        print(self._balance)
        print(self._ac)
c=Bankaccount("jyoti",660,1234568)
print(c.get_name("jyoti",669,243325256))
c.set_price(770)
c.display_info()
