# A five-digit number is entered through the keyboard.
# Write a program to obtain the reversed number and to determine whether the original and reversed numbers are equal or not.

UserInput=int(input("Enter any Five Digit Number:- "))
OrginalNumber=UserInput
ReversedNumber=0
while(UserInput!=0):
    reminder=UserInput%10
    ReversedNumber=(ReversedNumber*10)+reminder
    UserInput=UserInput//10
Equal_or_Not="original and reversed numbers are equal" if OrginalNumber==ReversedNumber else "original and reversed numbers are Not equal"   
print(Equal_or_Not) 