# Write a program to count the Number of matching characters in a pair of string

s1=input('Enter 1st string:')
s2=input('Enter 2nd string:')
sc=''
c=0
print('Matching char: ',end='')
for ch in s1:
    if ch in s2 and ch not in sc:
        c+=1
        sc+=ch
        print(ch,end=' ')
print('\nMatching char count:',c)