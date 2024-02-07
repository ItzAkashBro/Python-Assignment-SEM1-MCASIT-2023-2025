# Write a program to print out all Armstrong numbers between 1 and 500.

for number in range(1,500):
    ams=0
    orginal_number=number 
    while number>0:  
        reminder=number%10
        ams=(reminder**3)+ams
        number=number//10
    if(ams==orginal_number and ams!=1):
        print(f"{ams} is a amstrong number")

