# Write a program uppercase Half String

s=input('Enter a string:')
l=len(s)
print('New string is: ',(s[:l//2]).upper()+s[l//2:])