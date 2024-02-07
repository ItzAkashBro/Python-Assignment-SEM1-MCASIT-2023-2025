# Write a program to fill the entire screen with a smiling face.
# The smiling face has an ASCII value 1

import shutil
smiling_face = chr(1)
columns, rows = shutil.get_terminal_size()
grid = [[smiling_face] * columns for _ in range(rows)]
print("\n".join("".join(row) for row in grid))