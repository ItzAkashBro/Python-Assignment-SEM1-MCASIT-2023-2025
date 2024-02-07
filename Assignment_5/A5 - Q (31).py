# Write a program to find minimum number of rotations to obtain actual string

def min_rotations_to_actual_string(s):
    return min((s + s).find(s[i:i+len(s)]) for i in range(1, len(s) + 1)) or 0
str = input("Enter a string: ")
mr = min_rotations_to_actual_string(str)
print(f"The minimum number of rotations to obtain the actual string: {mr}")