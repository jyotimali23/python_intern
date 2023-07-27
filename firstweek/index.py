
n=int(input("enter the elements you want to add"))
lis=[]
for i in range(n):
	l=int(input("enter the your list"))
    import pdb ; pdb.set_trace()
	lis.append(l)
	lis.sort()
print(lis[-2])
print(sorted(set(lis)))
print(lis[-2])