def menu():
    on_off = True
    while on_off is True:
        print("_" * 40 + "\n" + " " * 8 + "EXERCISE 4 - MENU\n" + "_" * 40 + "\n" + " " * 7 + "1. Write input to file\n")
        print("       2. Write input to screen\n\n       3. Quit \n" + "_" * 40 + "\n")
        user_input = input("    From the menu, what do you want?\n\n    Enter your choice [1 - 3] : ")
        if not user_input.isdigit():
            user_input = input("\n    Choose 1, 2, or 3 from the menu: ")
        if user_input == "1":
            phrase1 = input("\n    Enter a phrase : ")
            with open("ex4_file", "w") as f:
                f.write(phrase1)
        elif user_input == "2":
            phrase2 = input("\n    Enter a phrase : ")
            print("_" * 40 + "\n\n" + "    The phrase you entered is:\n\n    %s \n\n" % phrase2)
        elif user_input == "3":
            print("\n\n    Thanks for stopping by, quitting now\n" + "_" * 40)
            on_off = False
    return
menu()