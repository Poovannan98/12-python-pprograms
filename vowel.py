# Hands on Experience Page No : 86
# 1. Write a program to check wheather the given character is a vowel or not.

ch = input("Enter the character : ")
if (ch.isalpha() == False):
    print("Error! Non-alphabetic character")
elif (ch == 'a' or ch == 'e' or ch == 'i' or 
      ch == 'o' or ch == 'u' or ch == 'A' or 
      ch == 'E' or ch == 'I' or ch == 'O' or 
      ch == 'U'):
    print("Given character is Vowel")
else:
    print("Given character is Consonant")
