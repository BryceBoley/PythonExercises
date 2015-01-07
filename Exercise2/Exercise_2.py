gas = raw_input("Please enter the number of gallons of gasoline: ")
gas = float(gas)
lit = gas * 3.7854
oil = gas / 19.5
CO2 = gas * 20
EtOH = (gas * 115000)/75700
cost = gas * 4.00
print "Original number of gallons is %f " % gas
print "%f gallons of gasoline is equivalent of %f liters" % (gas, lit)
print "%f gallons of gasoline requires %f barrels of oil" % (gas, oil)
print "%f gallons of gasoline produces %f pounds of CO2" % (gas, CO2)
print "%f gallons of gasoline is energy equivalent to %f gallons of ethanol" % (gas, EtOH)
print "%f gallons of gasoline requires %f US dollars" % (gas, gas * 4.00)
print "Thanks for playing this amazing game"