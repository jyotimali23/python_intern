# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an
x=lambda a:print("additon",a+15) 
print(x(10))
# argument, also create a lambda function that multiplies argument x with argument y and prints the result.
a=lambda x,y:print("multiply:",x*y)
print(a(4,8))
# 2.Write a Python program to find if a given string starts with a given character using Lambda.
x=lambda a: print(True) if a.startswith("the") else print(False)
print(x("the python is a programming langugae"))
# 3.What will be the output of the following Python code?
def san(x):
        print(x+1)
x=-2
x=4
san(12)
# 4.What will be the output of the following Python code?
def f():
    global a
    print(a)

    a = "hello"
    print(a) 
a = "world" 
f()
print(a)
# 5.Write a nested function called calculate_average that takes in a list of numbers as an argument 
# and calculates the average of those numbers
def outer_fun(average):
  lenght=len(average)
  average=sum(average)//lenght
  
  def inner_fun(calculate_average):
       print(calculate_average)
  inner_fun(average)   
outer_fun([2,3,4,5,6])
# 6.Write a nested function called validate_password that takes in 
# a password as an argument and checks if it meets the following criteria:
#    1.Contains at least one uppercase letter
# 2.Contains at least one lowercase letter
# 3.Contains at least one digit
# 4.Is at least 8 characters long
# The outer function should take user input for the password and call the nested
def outer(password):
    def inner(password):
        for i in password:
            if i.isupper() and i.islower():
                value=True
            elif i.isdigit() and len(password)>=8:
                value=True
            else:
                values=False
        print(values)
    inner(password)
password=input("enter the password")
outer(password)  
#2
def outer(password):
    def inner(password):
          v1=(any(map(str.isdigit,password)))
          v2=(any(map(str.islower,password)))
          v3=(any(map(str.isupper,password)))
          if v1 and v2 and v3==True and len(password)>8:
               print(True)
          else:
               print(False)
    
    inner(password)
password=input("enter the password")
outer(password) 

#  function to validate it. Finally, it should return a boolean value indicating whether the password is valid or not.
#  7. Use filter and map function with lambda to show the 
# of list with
# there sqaure values like:
# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result1 = map(lambda x: x *x, numbers)
result2= filter(lambda x:x * x,numbers)
print(list(result1))
print(list(result2))

