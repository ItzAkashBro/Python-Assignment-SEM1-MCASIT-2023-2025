# Write a Python function to check whether a number is perfect or not.

def per(num):
    return num > 0 and sum(i for i in range(1, num) if num % i == 0) == num
n = 28
print(f"{n} {'is' if per(n) else 'is not'} a perfect number.")