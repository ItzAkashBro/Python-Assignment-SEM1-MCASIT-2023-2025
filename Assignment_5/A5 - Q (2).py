# Write a program to take binary input numbers and 
# convert it to an integer without using int() function

import math
num=int(input('Enter a binary number:'))
p=0
i=0
while num>0:
    d=num%10
    i=i+d*pow(2,p)
    p+=1
    num//=10
print('Int number is: ',i)
