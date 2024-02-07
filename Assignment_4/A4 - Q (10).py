# Write a program in C to calculate factorial of a natural number.

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input('Enter a natural number:'))
if num<0:
    print('It\'s a negaive number.')
else:
    print(f'Factorial of {num} is: {fact(num)}')