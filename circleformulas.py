import math

def calcCirc(radius):
    return 2 * math.pi * radius

def calcArea(radius):
    return math.pi * radius ** 2

choice = input("What formula would you like to do? Circumference or area: ").capitalize()

while choice not in ['Circumference', 'Circ', 'Area']:
    choice = input("Invalid input. What formula would you like to do? Circumference or area: ").capitalize()

radius = float(input("Please provide the radius of the circle: "))

if choice == "Circumference":
    result = calcCirc(radius)
    print(f"The circumference is {result:f}")
elif choice == "Circ":
    result = calcCirc(radius)
    print(f"The circumference is {result:f}")
elif choice == "Area":
    result = calcArea(radius)
    print(f"The area is {result:f}")