import math
import supportingFunctions

def square_area():
    side = int(input("Enter the length of the sides."))
    return square_area

def retriangle_area():
    length = int(input("Enter the length of the side: "))
    width = int(input("Enter the width: "))
    return length*width

def circle_area():
    radius = int(input("Enter the radius: "))
    return math.pi*(radius**2)

def sphere_area():
    radius = int(input("Enter the raidus: "))
    return 4*math.pi*radius**2

def cone_area():
    radius = int(input("Enter the raidus: "))
    length = int(input("Enter the length: "))
    return math.pi*radius*(radius + length)

def cylinder_area():
    radius = int(input("Enter the radius: "))
    height = int(input("Enter the height: "))
    return 2*(math.pi*(radius**2)) + height*(2*math.pi*radius)

def area_menue():
    menue = """
1. Square area.
2. Rectriangle area.
3. Circle area.
4. Sphere area.
6. Cylinder area.
5. Cone area.
"""
    option = int(input(menue))
    option = Invalid_option(option, 5, menue)
    if option == 1:
        square_area()

def perimeter_menue():
    pass

def calculate_menue():
    menue = "Please choose an option to perform the following.\n1. Area\nPerimeter\n0. Exit"
    option = int(input(menue))
    option = Invalid_option(option, 2, menue)
    if option == 1:
        area_menue()
    elif option == 2:
        perimeter_menue()
    elif option == 0:
        print("Thank You.")
        return False
    print("Your task is completed.")
    calculate_menue()
    
