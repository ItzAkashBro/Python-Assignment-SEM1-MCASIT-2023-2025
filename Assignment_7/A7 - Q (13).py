# Write a Python program to reverse a string.

def rev(str):
    return str[::-1]
o = "Hello, World!"
r = rev(o)
print(f"The original string: {o}")
print(f"The reversed string: {r}")