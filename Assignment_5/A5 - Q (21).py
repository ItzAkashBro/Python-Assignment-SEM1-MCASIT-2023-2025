# Write a program to split and join a string

s=input('Enter a string:')
words = s.split()
js = '-'.join(words)
print("Original String:", s)
print("Split Result:", words)
print("Joined Result:", js)