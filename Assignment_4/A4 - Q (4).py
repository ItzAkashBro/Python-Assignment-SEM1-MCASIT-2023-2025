# Write a program in C to calculate H.C.F using while loop.

num1=int(input('Enter a number:'))
num2=int(input('Enter a number:'))

def hcf(n1,n2):
    hcf=1
    for i in range(2,n1):
        if n1%i==0 and n2%i==0:
            hcf=i
    return hcf

if num1<num2:
    print('HCF is:' ,hcf(num1,num2))
else:
    print('HCF is:' ,hcf(num2,num1))