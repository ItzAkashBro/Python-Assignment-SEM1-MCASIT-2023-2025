# Write a Python function to multiply all the numbers in a list

from functools import reduce
def mul(numbers):
    return reduce(lambda x, y: x * y, numbers, 1)
r = mul([2, 3, 4, 5])
print(f"The product is: {r}")