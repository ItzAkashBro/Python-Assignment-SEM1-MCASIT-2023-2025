# Write a program in C to print sum of all +ve numbers and all -ve numbers.

def sum():
    psum=0
    nsum=0
    while (1):
        num=int(input())
        if num==0:
            break
        elif num>0:
            psum+=num
        elif num<0:
            nsum+=num
        else:
            print('Invalid Number.')
    print('Sum of the positive number: ',psum)
    print('Sum of the negative number: ',nsum)
        
print('Enter positive and negative numbrs:')
sum()
    
    