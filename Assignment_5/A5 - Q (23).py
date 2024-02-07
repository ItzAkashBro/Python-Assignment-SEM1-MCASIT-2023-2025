# Write a program to find uncommon words from two Strings

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
uws = set(s1.split()).symmetric_difference(set(s2.split()))
print("Uncommon words:", uws)