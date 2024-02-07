# Write a program to swap commas and dots in a String

s= input("Enter a string with commas and dots: ")
r = s.translate(str.maketrans({',': '.', '.': ','}))
print("Original String:", s)
print("After swapping commas and dots:", r)
