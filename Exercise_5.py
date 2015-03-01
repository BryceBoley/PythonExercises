import string
from random import choice
from random import randint

for i in range(0, 10):
    random_integer = randint(0, 101)
    s = ""

    print("\n" + "* " * 15 + "Random String " + str(i + 1) + " has " + str(random_integer) + " characters " + "* " * 15)

    for j in range(0, random_integer):
        my_char = choice(string.ascii_letters)
        s += my_char
    print("\n" + s + "\n")

    with open("exercise_five.dat", "a+") as f:
        f.write(s + "\n")
        f.read()
        d = dict()
        for letter in s:
            d[letter] = d.get(letter, 0) + 1
            print(str(letter) + "=>" + str(d[letter]), end="")
        print("\n")
