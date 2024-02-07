# Write a Python function to find the max of three numbers.

def m3(num1, num2, num3):
    return max(num1, num2, num3)
n1, n2, n3 = 10, 25, 15
r = m3(n1, n2, n3)
print(f"The maximum  is: {r}")