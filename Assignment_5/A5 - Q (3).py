# WAP to remove i^th character of a string.

s1=input('Enter a string:')
i=int(input('Enter index to remove char:'))
s2=s1[:i]+s1[i+1:]
print('New string:',s2)