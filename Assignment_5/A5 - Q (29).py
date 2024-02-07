# Write a program to preform string slicing in Python to rotate a string

s = input("Enter a string: ")
ri = int(input("Enter the rotation index: "))
rs = s[ri:] + s[:ri]
print(f"Original String: {s}\nRotated String: {rs}")