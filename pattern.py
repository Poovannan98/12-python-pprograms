# Hands on Experience Page No : 86
# 7. Write a program to print the following pattern.
# *   *   *   *   *
# *   *   *   *
# *   *   *
# *   *
# *

i = 5;
while(i >= 1):
    for j in range(1,i+1):
        print('*',end='\t')
    print(end='\n')
    i -= 1;