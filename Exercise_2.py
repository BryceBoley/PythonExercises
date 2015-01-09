# getting user input and checking that it is a number and not zero
gas = raw_input("Welcome to the fun coversion tool! Please enter a whole number to represent gallons of gasoline: ")
while not gas.isdigit() or int(gas) == 0:
    gas = raw_input("Please enter a whole number, not zero, or non-numbers")

# math for conversions
gas = float(gas)
liter = gas * 3.7854
oil = gas / 19.5
co2 = gas * 20
etoh = (gas * 115000)/75700
cost = gas * 4.00

# print converted values to user using string formatting
print "Original number of gallons is %.1f " % gas
print "%.1f gallons is the equivalent of %.1f liters" % (gas, liter)
print "%.1f gallons of gasoline requires %.1f barrels of oil" % (gas, oil)
print "%.1f gallons of gasoline produces %.1f pounds of CO2" % (gas, co2)
print "%.1f gallons of gasoline is energy equivalent to %.3f gallons of ethanol" % (gas, etoh)
print "%.1f gallons of gasoline requires %.2f US dollars" % (gas, gas * 4.00)
print "Thanks for tyring the amazing conversion tool!"
