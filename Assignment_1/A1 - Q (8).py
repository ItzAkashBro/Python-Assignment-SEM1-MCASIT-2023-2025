# If a five-digit number is input through the keyboard,
# write a program to reverse the number.

UserNumber=int(input("Enter the Five digit Number\n"))
ReversedNumber=0
while(UserNumber>0):
    reminder=UserNumber%10
    ReversedNumber=(ReversedNumber*10)+reminder
    UserNumber=UserNumber//10
print(f"Reversed Number is :-{ReversedNumber}")
