# A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for
# 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after
# 30 days your membership will be cancelled. Write a program to accept the number of days
# the member is late to return the book and display the fine or the appropriate message.

days_late = int(input("Enter the number of days late: "))
if days_late <= 5:
    fine = 0.50 
elif days_late <= 10:
    fine = 1.00 
else:
    fine = 5.00
if days_late <= 30:
    print(f"The fine for returning the book {days_late} days late is Rs. {fine}")
else:
    print("Your membership has been cancelled due to late return.")
