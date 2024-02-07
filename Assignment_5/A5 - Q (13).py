# Write a program to maximum frequency character in String

s=input('Enter a string:')
d={}
for c in s:
    if c in d:
        d[c]+=1
    else:
        d[c]=1
min=max(d,key=d.get)
print('Maximum frequent character:',min,'frequent: ',d[min])