# Write a Python function to calculate the 
# factorial of a number (a non-negative integer). The
# function accepts the number as an argument.

def fac(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fac(number - 1)
n = 5
r = fac(n)
print(f"The factorial of {n} is: {r}")
