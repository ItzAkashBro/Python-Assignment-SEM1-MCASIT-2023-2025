# Write a program in C to check if a given number is even or odd using the function.

def evenodd(num):
    if num%2==0:
        print(num," is Even.")
    else:
        print(num," is Odd.")
num=int(input("Enter a Number:"))
evenodd(num)