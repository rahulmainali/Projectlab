"""Solve each of the following problems using Pyhton Scripts. Make sure you use appropriate variable
if names and comments. When there is a final answer have python print on the same screen. A person's body
mass index (BMI) is defined as: BMI=mass in kg / (height in m)/2"""

mass = float(input("enter the mass of the person in kg:"))
height = float(input("enter the height of the person in meter:"))
BMI = (mass/(height*height))
print(f"The BMI index of a person is {BMI}")
