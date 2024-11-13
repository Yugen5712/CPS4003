import files.draw
import files.calculate
import files.supportingFunctions

def main():
    menue = "Choose a option to perform:\n1. Calculate\n2. Draw.\n3. Exit."
    option = int(input("Choose a option to perform:\n1. Calculate\n2. Draw.\n3. Exit."))
    option = Invalid_option(option, 3, menue)
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "0":
        return True

if __name__ == "__main__":
    main()