# Write a Python program to filter a dictionary based on values.
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

o = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
t = 170
f = {key: value for key, value in o.items() if value > t}
print("Original Dictionary:", o)
print(f"Marks greater than {t}:", f)