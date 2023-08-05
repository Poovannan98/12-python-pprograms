# Hands on Experience Page No : 86
# Write a program to display Fibonacci series 0 1 1 2 3...

num = int(input("Enter the number : "))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print(end="\n")