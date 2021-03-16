# Write a python program to convert seconds to day, hour, minutes.

sec=int(input("Enter the second you want to convert into day, hour, minutes"))
day=sec/(60*60*24)
hour=sec/(60*60)
minute=sec/(60)
print(f"The day is {day}")
print(f"The hour is {hour}")
print(f"The minute is {minute}")