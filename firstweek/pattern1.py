for i in range(0,5):
	for j in range(1 ,8):
		if j>=6-i and j<=3+i:
			print("*",end="")
		else:
			print(" ",end="")
	print()