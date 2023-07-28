#difference between map filter and reduce
from functools import reduce
# m=[4.35,6.09,3.25 ,9.77,2.16,8.88,4.59]
n=[3.45,4.56,5.63,1.11,2.22,3.44,2.33]
# n1=list(map(lambda x:x*x,n))
# print(n1)
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# 1. Diff. Between Map filter and reduce
# 2. from functools import reduce
m=list(map(list,my_names))

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
print(m)

# Use filter to print only the names that are less than
# or equal to seven letters
#

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]


# Fix all three respectively.
map_result = list(map(lambda x: x, my_floats))
filter_result = list(filter(lambda name: name, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)


print(map_result)
print(filter_result)
print(reduce_result)
# result = list(map(round, n*n, range(1, 3)))
# print(result)

def is_A_student(names):
    return str(names)<=7

over= list(filter(is_A_student, my_names))

print(over)


