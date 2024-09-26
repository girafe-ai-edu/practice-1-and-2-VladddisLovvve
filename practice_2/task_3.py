# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""

#Additional detail 1:
print('Enter your weight in kg')
#
weight = input()
#Additional detail 2:
print('Enter your height in cm')
#
height = input()

#code here

weight=int(weight)
height=int(height)/100 #cm to m

bmi = round(weight/height**2, 2)

print(f'Your BMI equals to {bmi}')