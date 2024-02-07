# Write a program to take input a string of digits and
# convert it to an integer without using int() function.

snum=input('Enter a number:')
num=0
for c in snum:
    num=num*10+ord(c)-ord('0')
print('String converted to integer:',snum)