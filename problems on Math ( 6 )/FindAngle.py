#  ABC is a right triangle, 90 degree at .
# Therefore, .

# Point  is the midpoint of hypotenuse .

# You are given the lengths  and .
# Your task is to find  (angle , as shown in the figure) in degrees

import math 
AB = float(input())
BC = float(input())

MBC = str(round(math.degrees(math.atan2(AB, BC))))+u'\xb0'
print(MBC)
