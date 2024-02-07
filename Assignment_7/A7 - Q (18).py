# Write a Python function that takes a number as
# a parameter and check the number is prime or not.

def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
n = 17
print(f"{n} {'is' if is_prime(n) else 'is not'} a prime number.")