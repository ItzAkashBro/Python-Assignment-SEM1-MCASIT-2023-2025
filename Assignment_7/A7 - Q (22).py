# Write a Python function to create and print a list where the 
# values are square of numbers between 1 and 30 (both included)

def sq():
    return [num ** 2 for num in range(1, 31)]
r = sq()
print("List of square values:", r)