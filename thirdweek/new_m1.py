name = input("Enter your name: ")
fname = input("Enter your Father name: ")
college = input("Enter your college name: ")
rnumber = input("Enter your Roll number: ")
dd = int(input("Enter bdy date: "))
mm = int(input("Enter bdy month: "))
yyyy = int(input("Enter bdy year: "))
dmy = f"{dd}/{mm}/{yyyy}"
for i in range(70):
	print("-",end="")
	if i==69:
		for i in range(30):
			print("|")