name=str(input("Enter your name:"))
b=len(name)
if b<3:
    print("Name must be at least 3 characters")
elif b>50:
    print("Name must not exceed 50 characters")
else:
    print("Nice name")