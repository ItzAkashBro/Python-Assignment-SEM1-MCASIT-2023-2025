# Write a program to least Frequent Character in String

s=input('Enter a string:')
d={}
for c in s:
    if c in d:
        d[c]+=1
    else:
        d[c]=1
min=min(d,key=d.get)
print('Least frequent character:',min,'frequent: ',d[min])