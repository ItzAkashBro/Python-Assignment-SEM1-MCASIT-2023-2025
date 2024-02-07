# Write a program to capitalize the first and last character of each word in a string

s=input('Enter a string:')
s=s.split()
for w in s:
    l=len(w)
    if l==1 or l==2:
        s2=w.upper()
    else:
        s2=w[0].upper()+w[1:l-1]+w[l-1].upper()
    print(s2,end=' ')