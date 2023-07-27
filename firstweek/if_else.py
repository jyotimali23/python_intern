
amount=float(input("enter the total purachas amount:"))
if(amount>=100):
	dis=amount-(amount*10/100)
	print("discount",dis)
	total =amount-dis
	print("the discount of 10% is",total)
elif(amount>=50 and amount<100):
	dis=amount-(amount*5/100)
	print("discount",dis)
	total= amount-total
	print("the discount of 5% is",total)

else:
	 print("no discount applicable ")















































