# According to the Gregorian calendar, it was Monday on the date 01/01/1900.
# If any year is input through the keyboard
# write a program to find out what is the day on 1 st January of this year.

year = int(input("Enter the year: "))
if year < 1900:
    print("Please enter a year from 1900 onwards.")
else:
    q = 1
    K = year % 100
    J = year // 100
    day_of_week = (q + (13*(13+1)//5) + K + (K//4) + (J//4) - 2*J) % 7
    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(f"On January 1st, {year}, the day is {days_of_week[day_of_week]}.")
