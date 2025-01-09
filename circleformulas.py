choseCirc = "false"
choseArea = "false"
choseDiameter = "false"
choseRadius = "false"

choice = input("What formula would you like to do? Circumference, area, diameter, and radius: ").capitalize()

while choice not in ['Circumference', 'Area', 'Diameter', 'Radius']:
    choice = input("Invalid input. What formula would you like to do? Circumference, area, diameter, and radius: ").capitalize()

if choice == "Circumference":
    choseCirc = "true"
elif choice == "Area":
    choseArea = "true"
elif choice == "Diameter":
    choseDiameter = "true"
elif choice == "Radius":
    choseRadius = "Radius"

if choseCirc == "true":
    radius = input("Please provide the radius of the circle: ")
elif choseArea == "true":
    radius = input("Please provide the radius of the circle: ")
elif choseDiameter == "true":
    radius = input("Please provide the radius of the circle: ")
elif choseRadius == "true":
    radius = input("Please provide the radius of the circle: ")