lis1=[]
l=int(input("enter element"))
for i in range(l):
	ele=int(input())
	lis1.append(ele)
	lis1.sort()
print(lis1)

print(lis1[-2])
print(sorted(set(lis1)))
print(lis1[-2])