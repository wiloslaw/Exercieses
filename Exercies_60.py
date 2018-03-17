#60. Write a Python program to calculate the hypotenuse of a right angled triangle.

import os
import math

def przekatna(a,b):
    #import math
    przekatna = float(math.sqrt(a ** 2 + b ** 2))
    return przekatna


print("Najdluzszy bok trojkata to: ", przekatna(5,4))




#from math import sqrt
#print("Input lengths of shorter triangle sides:")
#a = float(input("a: "))
#b = float(input("b: "))

#c = sqrt(a**2 + b**2)
#print("The length of the hypotenuse is", c )
