# 10 Write a python program to find the sum of three integers. However, if two values are equal sum will be zero.

num1=int(input('Enter the first integers'))
num2=int(input('Enter the second integers'))
num3=int(input('Enter the third integers'))

sum=num1+num2+num3

if num1==num2 or num2==num3 or num1==num3:
    print("0")
else:
    print(f"The sum of three integers is:{sum}")
