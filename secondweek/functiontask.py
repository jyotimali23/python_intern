
''' create a function that accepts any number of numbers as positional arguments and prints the sum
of those numbers remember that we can use the sum function to add the values in an iterable
'''
def fun_1(*args):
        s=sum(args)
        return s
v=fun_1(12,23,34,45,67)
print(v)
''' creattes a fun that accepts any number postional arguments and that prints them 
 back to the user your output should indicates which values were provided as prostional arguments 
 and which were provided as keyword arguments '''
def fun_2(*args,**kargs):
    print(args)
    print(kargs)
fun_2("jyoti","dipti","aarti")
fun_2(name="jyoti",surname="mali")

'''
country={ "name":"germany"
"population":"berlin"
"capital" :"berlin"
"currency":"euro"
}'''
def fun_3(**kargs):
    my_dic={}
    for item in kargs.items():
        my_dic[item[0]] =item[1]
    print(my_dic)
fun_3(name="germany",populaion='83 million',capital='berlin',currency="euro")
def fun_4(**kargs):
    for keys,values in kargs.items():
        print("{}:{}".format(keys,values))

fun_4(name="germany",populaion='83 million',capital='berlin',currency="euro")
'''Using * unpacking and range, print the numbers 1 to 20, separated by commas
    . You will have to provide an argument for print function's sep parameter for this exercise.
'''
def fun_5():
    for i in range(1,21):
        print(i,end="")
fun_5()
def fun_5():
    for i in range(1,21):
        print(i)
fun_5()
'''6.Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 6.Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
7.Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12'''
def mul(l):
    r=1
    for i in l:
        r=i*r
    print(r)
mul([8,2,3,-1,7])
#check
def check(s):
    uppr=0
    lower=0
    for i in s:
        if i.isupper():
            uppr=uppr+1
        elif i.islower():
            lower=lower+1
    print(f"total no. of uppr is:{uppr}")
    print(f"total no. of lower is{lower}")
check('The quick Brow Fox')








