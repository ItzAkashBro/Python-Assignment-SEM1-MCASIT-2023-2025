# Create a function to calculate and return HCF of two numbers.

def hcf(x, y):
    return x if not y else hcf(y, x % y)
n1, n2 = 48, 60
r = hcf(n1, n2)
print(f"The HCF is: {r}")