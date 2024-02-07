# Write a Python program to access a function inside a function.

def outer(x):
    def inner(y):
        return y * 2
    return inner(x)
i = 3
o  = outer(i)
print(f"The result is: {o}")