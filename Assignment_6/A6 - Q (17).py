# Program to print all numbers which are divisible by M and N in the List.

l = [10, 15, 20, 25, 30, 35, 40]
M, N = 3, 5
r = [num for num in l if num % M == 0 and num % N == 0]
print(f"Numbers divisible by {M} and {N}:", r)