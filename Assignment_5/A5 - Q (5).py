# WAP to print even length words in a string.

s=input('Enter a String:')
s=s.split()
for w in s:
    if len(w)%2==0:
        print(w)