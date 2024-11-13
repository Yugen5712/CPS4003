def Invalid_option(option, x, menue):
    while option <= 0 or x <= option:
        print("Invalid option")
        try:
            option = int(input(menue))
        except ValueError:
            option = -1
    return option
