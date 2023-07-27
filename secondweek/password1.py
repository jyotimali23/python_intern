def outerfun(password):
	def innerfun(password):
		l,u,d=0,0,0
		if len(password)>=8:
			for i in password:
				if i.upper() and i.lower() :
					u=+1
					l=+1 
				if i.isdigit():
					d=+1
		if (u>=1 and l>=1 and d>=1):
				print("password is valid",password)
		else:
			print("password is invalid",password)
	innerfun(password)
password=input("enter the password")
outerfun(password)