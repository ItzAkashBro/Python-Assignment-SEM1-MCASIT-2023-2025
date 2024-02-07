# Write a program to enter the numbers till the user wants and at the end
# it should display the count of positive, negative and zeros entered.

pc = 0
nc = 0
zc = 0
while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    if num > 0:
        pc += 1
    elif num < 0:
        nc += 1
    else:
        zc += 1
print(f"\nCount of Positive Numbers: {pc}")
print(f"Count of Negative Numbers: {nc}")
print(f"Count of Zero Numbers: {zc}")