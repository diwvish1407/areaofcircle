# Write a Python program which accepts the radius of a circle from the user and computes area.

from math import pi
radius = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(radius) + " is: " + str(pi * radius**2))
