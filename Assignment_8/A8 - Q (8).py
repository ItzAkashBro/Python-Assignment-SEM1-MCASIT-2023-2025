# Write a Python program to get the maximum and minimum values of a dictionary.

d = {'a': 10, 'b': 5, 'c': 20, 'd': 8}
mk, mv = max(d.items(), key=lambda x: x[1])
mk, mv = min(d.items(), key=lambda x: x[1])
print("Dictionary:", d)
print("Max:", mv, "with key:", mk)
print("Min:", mv, "with key:", mk)