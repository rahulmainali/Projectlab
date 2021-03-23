weight=int(input("Enter your weight:"))

unit=input("(L)bs or (K)g :")

if unit.upper() == "L":
    converted_lbs=weight*0.45
    print(f"The person weight is{converted_lbs} kilos")
elif unit.upper() == "K":
    converted_kg=weight/0.45
    print(f"The person weight is{converted_kg} pounds")
else unit.upper() == "L":
    converted_lbs=weight*0.45
    print(f" Please enter appropriate character as K for Kg or L for lbs: ")