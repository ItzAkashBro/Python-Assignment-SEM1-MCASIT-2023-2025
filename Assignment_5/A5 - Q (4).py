# WAP to calculate the length of a string, avoid space.

s1=input('Enter a String:')
i=0
for c in s1:
    if c!=' ':
        i+=1
print('Length of the String:',i)