# Write a program to specific Characters Frequency in String List

s=input('Enter a string:')
d={}
for c in s:
    if c in d:
        d[c]+=1
    else:
        d[c]=1
for k,v in d.items():
    print(k,'frequent: ',v)