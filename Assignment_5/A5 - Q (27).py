# Write a program to word location in String

s = input("Enter a string: ")
t = input("Enter the word to find: ")
l = s.find(t)
print(f"The word '{t}' is located at index {l}." if l != -1 else f"The word '{t}' is not found in the string.")