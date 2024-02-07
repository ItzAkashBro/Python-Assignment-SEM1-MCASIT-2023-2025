# Python program to check if a string has at least one letter and one number

s=input('Enter a string:')
a=0
n=0
for c in s:
    if c>='A' and c<='Z' or c>='a' and c<='z':
        a+=1
    elif c>='0' and c<='9':
        n+=1
    else:
        print('Wron input.')
print(f'String has: {n} number {a} letter')