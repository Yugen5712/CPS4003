import math
import supportingFunctions

def area_menue():
    menue = """
1. Square area.
2. Rectriangle area.
3. Circle area.
4. Sphere area.
5. Cone area.
"""

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
    
