# Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

d1 = {'key1': 1, 'key2': 3, 'key3': 2}
d2 = {'key1': 1, 'key2': 2}
c = set(d1) & set(d2)
for key in c:
    if d1[key] == d2[key]:
        print(f"{key}: {d1[key]} is present in both dictionaries.")