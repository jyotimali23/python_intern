n=int(input("enter the number"))
for i in range(n):
	if i<=n//2:
		print(" "*(n-i) + "* "*i)
	else:
		print(" "*i +"* "*(n-i))