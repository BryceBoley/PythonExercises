# a_string = "akeuhwLWEEPOLSVLJKBAKppoqyituvmalkmzlajdgwoqpeyYEWY6DBVJIU"
#
# d = dict()
# for c in a_string:
#     d[c] = d.get(c,0) + 1
# print d

import string
from random import choice
from random import randint

random_integer = randint(0, 101)
s = ""

for i in range(0, randint(0, 101)):
    my_char = choice(string.letters)
    s += my_char

#put the string generator into a function




