# Write a program to generating random strings until a given string is generated

import random
import string
ts = input("Enter the target string: ")
while True:
    rs = ''.join(random.choice(string.ascii_lowercase) for _ in range(len(ts)))
    print("Generated:", rs)
    if rs == ts:
        break
print("Target string generated!")