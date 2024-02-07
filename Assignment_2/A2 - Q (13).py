# Any year is entered through the keyboard, write a program to determine whether the year is
# leap or not. Use the logical operators && and ||.

year=int(input("enter any year"))
if(year%4==0 or year%400==0) and (year%100!=0):
    print("this is a leap year")
else:
    print("not a leap year")