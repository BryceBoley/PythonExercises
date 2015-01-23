speed = raw_input("Please enter a number to represent miles/hour: ")

while not speed.isdigit():
    speed = raw_input("A number to represent miles/hour, please: ")
speed = float(speed)

# meter = 117.647 barleycorns
# mile = 1609.34 meter
# mile = 189334.02298 barleycorns
# bd = barleycorns per day
bd = 189334.02298 * speed * 24
# furlong = 220 yards
# yard = 0.9144 meter
# fortnight = 14 days = 336 hours
# 1 mile = 7.99998011612 furlongs
# ff = furlongs per fortnight
ff = 7.99998011612 * speed * 336
# mach1 = 1130 ft/sec
# 1 mph = 1.46666666667 ft/sec
mach = (speed * 1.46666666667) / 1130
# 1 mph = 0.44704 meters/sec
# psl = 299792458 meters/sec
psl = (speed * 0.44704) / 299792458


print "_" * 70 + "\n" + "Original speed in mph is: %.1f" % speed
print "\nConverted to barleycorns per day is: %.3e" % bd
print "Converted to furlongs per fortnight is: %.3e" % ff
print "Converted to Mach number is: %.3e" % mach
print "Converted to percentage of the speed of light is: %.3e" % psl
print "_" * 70 + "\n" + "Thanks for playing, I hope you learned something, I did!"
