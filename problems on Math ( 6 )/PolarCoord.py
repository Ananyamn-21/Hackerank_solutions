# Task
# You are given a complex . Your task is to convert it to polar coordinates.

# Input Format

# A single line containing the complex number . Note: complex() 
# function can be used in python to convert the input as a complex number.
import cmath
number = input()

print(cmath.polar(complex(number))[0])
print(cmath.polar(complex(number))[1])