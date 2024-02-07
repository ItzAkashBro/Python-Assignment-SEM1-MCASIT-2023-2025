# Write a program to find the octal equivalent of the entered number.

number = int(input("Enter a number: "))
remainder = [0] * 100
i = 0
while number > 0:
    remainder[i] = number % 8
    number = number // 8
    i = i + 1
print("Octal equivalent of the entered number is: ", end="")
for j in range(i - 1, -1, -1):
    print(remainder[j], end="")