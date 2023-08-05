# Hands on Experience Page No : 86
# 2. Using if..else..elif statement check smallest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b and a < c:
    print("Smallest number is:", a)
elif b < a and b < c:
    print("Smallest number is:", b)
else:
    print("Smallest number is:", c)