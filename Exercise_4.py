# true to turn on the while loop
user_input = True
while user_input:
    print ("""
    ********************************
    EXERCISE 4 - MENU
    ********************************
    1. Write input to file
    2. Write input to screen
    3. Quit
    ********************************
    """)
    user_input = raw_input("What do you want to do?  Enter your choice [1 - 3] : ")
# if input isnt a number 1-3
    while not user_input.isdigit():
        user_input = raw_input("Choose 1, 2, or 3 from the menu: ")
    if user_input == "1":
        phrase1 = raw_input("Enter a phrase: ")
        with open("ex4_file", "w") as f:
            f.write(phrase1)
    elif user_input == "2":
        phrase2 = raw_input("Enter a phrase: ")
        print "You entered: '%s' " % phrase2
    elif user_input == "3":
        print("Ok, thanks for stopping by, quitting now")
        user_input = False
