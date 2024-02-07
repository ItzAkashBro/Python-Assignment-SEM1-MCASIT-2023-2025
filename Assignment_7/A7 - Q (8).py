# Create a function to calculate and return LCM of two numbers.

def lcm(x, y):
    gcd = lambda a, b: a if not b else gcd(b, a % b)
    lcm = (x * y) // gcd(x, y)
    return lcm
n1, n2 = 12, 18
r = lcm(n1, n2)
print(f"The LCM is: {r}")