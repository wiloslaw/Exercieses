#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def suma(x, y, z):
    if x == z or x == y or z == y:
        suma = 0
    else:
        suma = x + y + z
    return suma

print(suma(1, 1, 2))
print(suma(1, 2, 3))
print(suma(2, 2, 3))





