# Write a program to string slicing in Python to check
# if a string can become empty by recursive deletion

def cbe(s):
    return s == "" or any(cbe(s[:i] + s[i+1:]) for i in range(len(s)))
str = input("Enter a string: ")
if cbe(str):
    print("The string can become empty by recursive deletion.")
else:
    print("The string cannot become empty by recursive deletion.")