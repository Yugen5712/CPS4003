def main():
    option = input("Choose a option to perform:\n1. Calculate\n2. Draw.\n3. Exit.")
    while option not in ["1", "2", "0"]:
        print("Invalid option please choose the correct option.")
        option = input("Choose a option to perform:\n1. Calculate\n2. Draw.\n3. Exit.")
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "0":
        return True

if __name__ == "__main__":
    main()