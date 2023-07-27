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
     n=len(name)
     n1=len(fname)
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
      print("please enter a valid number",ve)
    else:
      print("+","-"*100,"+")
      print("\t\tCOLLEGE: ", college)
      print("|","Name:-",name," "*(20-n),"|","FATHER NAME:-",fname," "*(54-n1),"|")
      #print("|","Date Of Birth:-",dmy," "*(20-n),"|","ROll number:-",rollno," "*(54-n1),"|")
      print("\n\t\tROLL NUMBER: ", rnumber)
      print("\n\t\t SUBJECTS \tMArks \tTOTAl \tGRADES")
      for b, e,f,g in zip(subject,Marks,Total,grades):
        print("\n\t\t", b, " \t",e, " \t",f,"\t",g)
        e=e+1
    MTotal=MTotal+e
    totalno=500
    percentage=(MTotal/totalno)*100
    print("\n\t\tTOTAL MARKS: ",MTotal , "\t\t| ")
    print("\n\t\tPERCENTAGE:", percentage, "\t\t|:")
    break