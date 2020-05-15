from math import sqrt

def hypotenuse(a, b):
    return sqrt(a ** 2 + b ** 2)

a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))

print("The hypotenuse of the triangle is", hypotenuse(a, b))