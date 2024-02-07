# Write a program to odd Frequency Characters

s=input('Enter a string:')
d={}
for c in s:
    if c in d:
        d[c]+=1
    else:
        d[c]=1
for k,v in d.items():
    if v%2!=0:
        print('odd freq character:',k,'frequent: ',v)