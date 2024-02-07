# When interest compounds q times per year at an annual rate of r % for n years, the principle p
# compounds to an amount a as per the following formula. Write a program to read 10 sets of p, r,
# n & q and calculate the corresponding as.
# a=p(1+r/q)^np

sets = 10
for i in range(sets):
    p = int(input("Enter the principle: "))
    r = float(input("Enter the Interest rate: "))
    n = int(input("Enter the Year: "))
    q = int(input("Enter number of times interest compounds per year: "))
    a = p * (1 + r / q) ** (n * q)
    print(f"Compound Interest for set {i + 1}: {a}")