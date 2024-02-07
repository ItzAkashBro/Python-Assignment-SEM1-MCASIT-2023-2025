# Any year is input through the keyboard.
# Write a program to determine whether the year is a leap year or not.

Year=int(input("Enter The Year:- "))
Leap_or_Not="This Is a Leap Year" if Year%4==0 else "This Is Not a Leap Year"
print(Leap_or_Not)