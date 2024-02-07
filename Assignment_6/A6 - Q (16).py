# Program to Create two lists with EVEN numbers and ODD numbers from a list.

l = [10, 15, 20, 25, 30]
e, o = [num for num in l if num % 2 == 0], [num for num in l if num % 2 != 0]
print("Even Numbers:", e)
print("Odd Numbers:", o)