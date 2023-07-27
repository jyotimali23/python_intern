#pass by value
# def my_funct(args):
# 	args+=100
# 	return args
# int1=100
# print(int1)
# var =my_funct(int1)
# print(var)
# print(int1)
#pass by refreces

# def my_fun(list1,int1=100):
# 	list1.append("b")
# 	return list1 

# list1=['a']
# var=my_fun(list1)
# print(list1) 	
def my_fun(**lan):
	for key,value in lan.items():
		print(key,value)
vaar=my_fun(name='jyoti',surname='mali')
print(vaar)

 #printdic={'a':1,'b':2,'c':3}
#for keys ,values in dic.items():
	#(f"{keys}={values})
def fun2(name):
	return name
s=fun2("jyoti")
print(s)
def fun3(**kargs):
	for key,value in kargs.items():
		print({key:value})

fun3(name="jyoti",surname="mali",name1="dipti",surname1="mali")
#addition
def fun3(*numbers):
	for i in numbers:
		sum=sum+i
		return sum
fun3(2,3,4,5,6,6,7)