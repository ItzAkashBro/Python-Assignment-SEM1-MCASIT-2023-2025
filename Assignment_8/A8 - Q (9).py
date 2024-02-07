# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'MCA1stsem'
# Expected output: {'M':1,'C':2,'A':3,'1':4,'s':5,'t':6,'s':7,'e':8,'m':10}

s = 'MCA1stsem'
c = {char: index + 1 for index, char in enumerate(s)}
print("Sample string:", s)
print("Resulting dictionary:", c)