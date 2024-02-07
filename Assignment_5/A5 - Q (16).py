# Write a program to frequency of numbers in String

s=input('Enter a string:')
c=0
for k in s:
    if k>='0' and k<='9':
        c+=1
print('Number frequent: ',c)