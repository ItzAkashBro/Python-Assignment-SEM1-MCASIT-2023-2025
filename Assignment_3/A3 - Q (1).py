# Write a program to calculate overtime pay of 10 employees. Overtime is paid at the rate of Rs.
# 12.00 per hour for every hour worked above 40 hours. Assume that employees do not work for
# fractional part of an hour.

for i in range(1,11):
    TotalWork=int(input(f"Enter Work duration for {i} employee: "))
    if(TotalWork>40):
        overtime=TotalWork-40
        overtimePay=overtime*12
        print(f"Your overtime pay is {overtimePay}")
    else:
        print("this employee does not do overtime")
