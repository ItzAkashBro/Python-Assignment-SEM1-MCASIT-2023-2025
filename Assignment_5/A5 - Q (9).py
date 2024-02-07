# Write a program to accept the strings which contain all vowels

s=input('Enter a string:')
c=1
for i in ['a','e','i','o','u']:
    if i not in s:
        c=0
if c==1:
    print('String is accepted.')
else:
    print('String is not accepted.')