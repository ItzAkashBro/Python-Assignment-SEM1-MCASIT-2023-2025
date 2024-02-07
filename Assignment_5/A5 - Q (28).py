# Write a program to find consecutive characters frequency

s = input("Enter a string: ")
c = {}
p= None
[c.setdefault(char, c.get(char, 0) + 1) for char in s if char == p or not (p := char)]
print("Consecutive Character Frequency:")
print('\n'.join(f"{char}: {count}" for char, count in c.items()))