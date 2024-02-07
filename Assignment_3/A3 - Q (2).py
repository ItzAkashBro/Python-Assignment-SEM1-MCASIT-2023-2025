# Write a program to find the factorial value of any number entered through the keyboard.

def fact(n):
    if n==0 or n==1:
        return n
    else:
        return n*fact(n-1)
n=int(input("enter any number "))
print(f"factorial is {fact(n)}")