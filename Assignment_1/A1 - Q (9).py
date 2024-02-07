# If a four-digit number is input through the keyboard,
# write a program to obtain the sum of the first and last digit of this number.

UserInput=int(input("Enter Any Four Digit Number To Get The Sum:- "))
if(len(str(UserInput))==4):
    FirstDigit=UserInput//1000
    LastDigit=UserInput%10
    print("Sum Of the First And Last digit of Your Entered Number is:- ",FirstDigit+LastDigit)
else:
    print("You entered wrong Value")