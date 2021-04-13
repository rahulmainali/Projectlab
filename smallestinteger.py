# Given three integers, print the smallest one. (Three integers should be user input)
a=int(input("Enter the first integer"))
b=int(input("Enter the second integer"))
c=int(input("Enter the third integer"))

if a<b<c:
    print("A is the smallest integer")
elif b<a<c:
    print("B is the smallest integer")
else:
    print("C is the smallest integer")