# Write a Python function that takes a list and 
# returns a new list with unique elements of the first list.

def unique(input_list):
    return list(set(input_list))
o = [1, 2, 2, 3, 4, 4, 5]
r = unique(o)
print(f"Original List:", {o})
print(f"Unique List:", {r})