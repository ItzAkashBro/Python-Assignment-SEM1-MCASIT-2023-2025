# Write a Python program to print the even numbers from a given list.

def pe(i):
    e = [num for num in i if num % 2 == 0]
    print(f"Even numbers in the list: {e}")
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pe(n)