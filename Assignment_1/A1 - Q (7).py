# If a five-digit number is input through the keyboard, 
# Write a program to calculate the sum of it's digits.(Hint: Use the modulus operator ‘%’)

sum = 0
num = int(input("Enter 5 digit number:"))
sum = (num%10)+(num//10)%10 + (num//100)%10+(num//1000)%10+(num//10000)
print("Sum of the digit is:", sum)
    