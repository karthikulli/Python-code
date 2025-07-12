def sessional_marks(Sessional_1,Sessional_2):
    if Sessional_1>Sessional_2:
        s1=(Sessional_1/100)*80
        s2=(Sessional_2/100)*20
        sessional_total=s1+s2
    else:
        s1=(Sessional_1/100)*20
        s2=(Sessional_2/100)*80
        sessional_total=s1+s2
    return sessional_total
def assignment_quiz_marks(Assignment_1,Assignment_2,Quiz_1,Quiz_2):
    marks_obtained=Assignment_1+Assignment_2+Quiz_1+Quiz_2
    Assignment_quiz_total=(marks_obtained*7)/48
    return Assignment_quiz_total
def Attendence_calculator(Attedence):
    if Attedence>=90:
        Attedence_marks=5
    elif Attedence>=85 and Attedence<90:
        Attedence_marks=4
    elif Attedence>=80 and Attedence<85:
        Attedence_marks=3
    elif Attedence>=75 and Attedence<80:
        Attedence_marks=2
    else:
        Attedence_marks=0
    return Attedence_marks
    
Sessional_1=float(input("Enter Sessional_1 marks: "))
Sessional_2=float(input("\nEnter Sessional_2 Marks: "))
Assignment_1=float(input("\nEnter Assignment_1 Marks: "))
Assignment_2=float(input("\nEnter Assignment_2 Marks: "))
Quiz_1=float(input("\nEnter Quiz_1 Marks: "))
Quiz_2=float(input("\nEnter Quiz_2 Marks: "))
Attedence=int(input("\nEnter Attedence percentage: "))
Sessional_marks=sessional_marks(Sessional_1,Sessional_2)
Assignment_quiz_marks=assignment_quiz_marks(Assignment_1,Assignment_2,Quiz_1,Quiz_2)
Attedence_marks_calculator=Attendence_calculator(Attedence)
total_marks=round((Sessional_marks+Assignment_quiz_marks+Attedence_marks_calculator),2)
print("\nTotal Marks: ",total_marks)
