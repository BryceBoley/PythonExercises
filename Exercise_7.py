d = {
    "Boston": "0 C",
    "Boise": "48 F",
    "Phoenix": "85 F",
    "Miami": "40 C",
    "Riverside": "30 C",
    "Baltimore": "32 F",
}


def ctof(c):
    f_temp = float(c) * 9/5+32
    return f_temp


def ftoc(f):
    c_temp = ((float(f) - 32.0)*5.0/9)
    return c_temp


for x in d:
    y = d.get(x)
    if y[-1] == "C":
        z = ctof(int(y[0:2]))
        print("In %s it is %s degrees Celsius,\n\t which is equivalent to %s degrees Fahrenheit\n" % (x, y[0:2], z))
    elif y[-1] == "F":
        z = ftoc(int(y[0:2]))
        print("In %s it is %s degrees Fahrenheit,\n\t which is equivalent to %s degrees Celsius\n" % (x, y[0:2], z))