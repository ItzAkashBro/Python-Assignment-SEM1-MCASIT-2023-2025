#Any integer is input through the keyboard.
#Write a program to find out whether it is an odd number or even number.

UserInput=int(input("Enter Any Integer:- "))
Even_Or_Odd= "Even" if UserInput%2==0 else "Odd"
print(f"Your Entered Integer is:- {Even_Or_Odd}")