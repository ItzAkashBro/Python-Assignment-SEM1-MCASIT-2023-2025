# An Insurance company follows following rules to calculate premium.
# • If a person’s health is excellent and the person is between 25 and 35 years of age and lives in a city and is a male then the premium is Rs. 4 per thousand and his policy amount cannot exceed Rs. 2 lakhs.
# • If a person satisfies all the above conditions except that the sex is female then the premium is Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh.
# • If a person’s health is poor and the person is between 25 and 35 years of age and lives in a village and is a male then the premium is Rs. 6 per thousand and his policy cannot exceed Rs. 10,000.
# • In all other cases the person is not insured.
# Write a program to output whether the person should be insured or not, his/her premium ratemand maximum amount for which he/she can be insured.

A=int(input("enter age: "))
g=input("enter gender (M/F): ")
c=input("Reside in city? (Y/N): ")
h=input("enter Health Condition (excelent/poor): ")
if(A>=25 and A<=35 and h=="excelent" and c=="Y" and g=="M"):
    print("premium Rs. 4/1000 and max policy amount Rs. 2 lakhs.")
elif(A>=25 and A<=35 and h=="excelent" and c=="Y" and g=="F"):
    print("premium Rs. 3/1000 and max policy amount Rs. 1 lakh.")
elif(A>=25 and A<=35 and h=="poor" and c=="N" and g=="M"):
    print("premium Rs. 6/1000 and max policy amount Rs. 10,000.")
else:
    print("Not eligible")