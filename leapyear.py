# Test whether it is a leap year or not.

day=int(input("Enter the number of days in a year"))
if day%4==0:
    print("It is a leap year")
else:
    print("It is a common year")