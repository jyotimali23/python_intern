while True:
    try: 
     name = input("Enter your name ")
     fname = input("Enter your Father name")
     rnumber = input("Enter your Roll number ")
     college = input("Enter your college name ")
     subject = ["Physics","MATHS", "CHEMISTRY","HINDI","ENGLISH"]
     Marks = []
     Total = []
     grades=[]
     MTotal = 0
     n1=len(name)
     n2=len(fname)
     h="Higher Secondary Education board"
     b="bhopal"
     b1=len(b)
     b3=int(b1/2)
     h1=len(h)
     h2=int(h1/2) 
     s1=30+(n1+n2)
     s2 = int(s1/2)
     for x in subject:
        a = int(input("Enter marks for " + x))
        Marks.append(a)
        for y in Marks:
           Total.append(a)
           for z in Marks:
                if(z>=80):a="A"
                elif(z>=60):a="B"
                elif(z>=40):a="C"
                elif(z>=30 ):a="D"
                else:a=("F")
                grades.append(a)
    except ValueError as ve:
      print("please valid number",ve)
    else:
      print("+","-"*s1,"+")
      print("|"," " *(s2-h2),h, " "*(s2-h2),"|")
      print("|"," "*(s2-b1),b,(s2-b1)*" ","|")

      print("|"," "*int(n1+n2/2),"NAME: ", name,"|","FATHER NAME: ", fname," "*int(n1+n2/2),"|")
      print("\n\t\tROLL NUMBER: ", rnumber)
      print("\n\t\t SUBJECTS \tMArks \tTOTAl \tGRADES")   
      for b2, e,f,g in zip(subject,Marks,Total,grades):
        print("\n\t\t", b2, " \t",e, " \t",f,"\t",g)
        
      MTotal=MTotal+y
      totalno=500
      break
    #percentage=(MTotal/totalno)*100
    #print("\n\t\tTOTAL MARKS: ",MTotal , "\t\t| ")
    #print("\n\t\tPERCENTAGE:", percentage, "\t\t|:")