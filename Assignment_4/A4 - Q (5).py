# Write a program in C to calculate l.c.m using while loop.

num1=int(input('Enter a number:'))
num2=int(input('Enter a number:'))

def lcm(n1,n2):
    lcm=n1
    while True:
        if lcm%n1==0 and lcm%n2==0:
            break
        lcm+=n1
    return lcm

if num1>num2:
    print('LCM is:' ,lcm(num1,num2))
else:
    print('LCM is:' ,lcm(num2,num1))