name=input("Enter your name")
fathername=input("Enter your father name")
Schoolname=input("Enter your Schoolname")
rollno=int(input( "Enter your Rollno"))
dd=int(input("enter bdy date"))
mm=int(input("Enter bdy month"))
yyyy=int(input("Enter bdy year"))
dmy=(f"{dd}/{mm}/{yyyy}")
physicsno=int(input( "Enter your Physicsno"))
mathsno=int(input("Enter your mathsno"))
chemistryno=int(input("Enter your chemistry"))
hindino=int(input("Enter your hindino"))
englishno=int(input("Enter your englishno"))
for grades in range(physicsno):
   if(grades>=80):grades="A"
   elif(grades>=60):grades="B"
   elif(grades>=40):grades="C"
   elif(grades>=30 ):grades="D"
   else:grades=("F")
for grades1 in range(mathsno):
    if(grades1>=80):grades1="A"
    elif(grades1>=60):grades1=" B"
    elif(grades1>=40 and grades1<60):grades1="C"
    elif(grades1>=30 and grades1<40):grades1="D"
    else:grades1="F"
for grades2 in range(chemistryno):
    if(grades2>=80):grades2="A"
    elif(grades2>=60):grades2= "B"
    elif(grades2>=40):grades2="C"
    elif(grades2>=30 and grades2<40):grades="D"
    else:grades2=("F")
for grades3 in range(hindino):
    if(grades3>=80):grades3="A"
    elif(grades3>=60 ):grades3= "B"
    elif(grades3>=40 ):grades3="C"
    elif(grades3>=30 ):grades3="D"
    else:grades3=("f")
for grades4 in range(englishno):
    if(grades4>=80):grades4="A"
    elif(grades4>=60 ):grades4= "B"
    elif(grades4>=40 ):grades4="C"
    else:grades4=("F")
totalmarksA=physicsno+mathsno+chemistryno+hindino+englishno
totalno=500
percentage=(totalmarksA/totalno)*100
n=len(name)
n1=len(fathername)
print("+","-"*100,"+")
print("|"," "*30,"Higher Secondary Education board "," "*35,"|")
print("|"," "*40, "(Bhopal)"," "*50,"|")
print("+","-"*100,"+")
print("|"," "*40,"MARKSHEET"," "*49,"|")
print("+","-"*100,"+")
print("|","Name:-",name," "*(20-n),"|","FATHER NAME:-",fathername," "*(54-n1),"|")
print("|","Date Of Birth:-",dmy," "*(20-n),"|","ROll number:-",rollno," "*(54-n1),"|")
print("ROll number:-",rollno," "*41,"|")
print("|"," "*4,"School Name:-  ",Schoolname," "*6,"|"," "*60,"|")
print("+","-"*100,"+")
print(" |Subject","\n","Physics","\n","| MATHS","\n","| CHEMISTRY","\n","| HINDI","\n","| ENGLISH",end="")
print(" |Marks","|",physicsno,"|",mathsno,"|",chemistryno,"|",hindino,"|",englishno)
print("| Total","|",physicsno,"|",mathsno,"|",chemistryno,"|",hindino,"|",englishno)