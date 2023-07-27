numbers=range(1,21)
print(*numbers,sep=",")
numers1=range(1,21)
print(*numbers,sep='\n')

def fun_2(*args,**kargs):
       print(args, kargs)
fun_2("jyoti","dipti","aarti")
fun_2(name="jyoti",surname="mali")
