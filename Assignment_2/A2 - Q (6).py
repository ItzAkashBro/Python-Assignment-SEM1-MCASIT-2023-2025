# If the ages of Ram, Shyam and Ajay are input through the keyboard,
# write a program to determine the youngest of the three.

RamAge=int(input("Enter Age Of Ram:- "))
ShyamAge=int(input("Enter Age Of Shyam:- "))
AjayAge=int(input("Enter Age Of Ajay:- "))

if(RamAge<ShyamAge and RamAge<AjayAge):
    print("Ram is Youngest with the age of:- ",RamAge)
elif(ShyamAge<RamAge and ShyamAge<AjayAge):
    print("Shyam is Youngest with the age of:- ",ShyamAge)
elif AjayAge < RamAge and AjayAge < ShyamAge:
    print("Ajay is Youngest with the age of:- ", AjayAge)
else:
    print("There are people with the same youngest age.")