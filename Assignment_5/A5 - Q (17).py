# Write a program to program to check if a string contains any special character

s=input('Enter a string:')
print('Special Character: ')
i=1
for c in s:
    if (c>='!' and c<'0') or (c>'9' and c<'A') or (c>'Z' and c<'a') or (c>'z' and c<='~'):
        print(c,end=' ')
        i=0
if i==1:
    print('Not include.')