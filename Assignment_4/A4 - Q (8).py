# Write a program in C to calculate combinatoric C(n,r) using function.

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
def combinatoric(n,r):
    if n<r:
        return 0
    else:
        return fact(n)//fact(r)*(fact(n-r))
n=int(input('Enter n value: '))
r=int(input('Enter r value: '))

print(f'C({n},{r})={combinatoric(n,r)}')