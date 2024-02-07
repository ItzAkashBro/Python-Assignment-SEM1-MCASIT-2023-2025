# Write a program to remove all duplicates from a 
# given string in Python, keeping the first character only

s=input('Enter a string:')
ns=''
for c in s:
    if c not in ns:
        ns+=c
print('New String: ',ns)