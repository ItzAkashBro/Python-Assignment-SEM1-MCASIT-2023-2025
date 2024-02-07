# Write a program in C to check whether an inputted number is palindrome.

def pal(num):
    rev=0
    temp=num
    while temp>0:
        d=temp%10
        rev=rev*10+d
        temp//=10
    if num==rev:
        return 1
    else:
        return 0
print('Enter a Number:')
num=int(input())
if pal(num)==1:
    print(num,' is a palindrome number.')
else:
    print(num,' is a not palindrome number.')