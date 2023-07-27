emloye_salary= float(input("enter your salary"))
employe_year=int(input("enter your year"))
if employe_year>=5:
     bonus=emloye_salary*5/100
     print("congratulationus you got bonus",bonus)
     print("your total salary is",emloye_salary+bonus)
     
     
else:
     print("you donot got bonus")