import urllib2
import string
from string import digits


def string_word_frequency():
    #with open('exercise_five.txt')as f:
    f= urllib2.urlopen('http://www.gutenberg.org/files/10/10.txt').read()
        # f = f.read()
    f_out = f.translate(string.maketrans("", ""), string.punctuation).lower().translate(None, digits)

    d = dict()
    for i in f_out.split():
        d[i] = d.get(i, 0) + 1
    for word in sorted(d, key=d.get, reverse=True):
         print word, d[word]
    # return
    f.close()
string_word_frequency()