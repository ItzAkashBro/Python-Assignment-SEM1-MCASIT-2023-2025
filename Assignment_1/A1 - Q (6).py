# Two numbers are input through the keyboard into two locations C and D. 
# Write a program to interchange the contents of C and D.

c=int(input("Enter Number for C= "))
d=int(input("Enter Number for D= "))
c=c+d
d=c-d
c=c-d
print(f"Number in C is = {c} and Number in D is ={d}")