# Write a program to print permutation of a given string using inbuilt function

from itertools import permutations
s = input("Enter a string: ")
print(f"Permutations of '{s}':")
for ps in permutations(s):
    print(''.join(ps))