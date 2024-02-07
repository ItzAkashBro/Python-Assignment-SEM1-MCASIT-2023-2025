# Ramesh’s basic salary is input through the keyboard.
# His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary.
# Write a program to calculate hisgross salary

# Ans=
BS = float(input("Enter Ramesh's basic salary: "))
DA = 0.4 * BS
HRA = 0.2 * BS
GS = BS + DA + HRA
print("Ramesh's Gross Salary is:", GS)