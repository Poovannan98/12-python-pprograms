# Hands on Experience Page No : 86
# 6. Write a program to check if the given number is a palindrome or not.

number = int(input("Enter a number: "))
 
reverse = 0
temp = number
while (temp != 0):
    reverse = (reverse * 10) + (temp % 10)
    temp = temp // 10

if number == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")