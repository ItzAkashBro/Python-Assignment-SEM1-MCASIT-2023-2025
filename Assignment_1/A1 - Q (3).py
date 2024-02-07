# If the marks obtained by a student in five different subjects are input through the keyboard,
# find out the aggregate marks and percentage marks obtained by the student.
# Assume that the maximum marks that can be obtained by a student in each subject is 100.

TotalMarks=0
sno=1
for i in range(5):
    Mark=int(input(f"Enter The {sno} Subject Marks: "))
    TotalMarks=Mark+TotalMarks
    i=i+1
    sno=sno+1
print(f"total marks Obtained By the Student is {TotalMarks} and Percentage is :-",(TotalMarks/500)*100)
