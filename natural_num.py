# Hands on Experience Page No : 86
# Write a program to display sum of natural numbers, upto n.

number = int(input("Enter the Number : "))
sum = 0
x = 1
while x <= number:
	sum = sum + x
	x = x + 1
print("Sum of Given number is : ",sum)