num1 = int(raw_input("Please enter first integer:"))
while num1 == 0:
    print("invalid number")
    num1 = int(raw_input("Please enter first integer:"))
num2 = int(raw_input("Please enter second integer:"))
while num2 == 0:
    print("invalid number")
    num2 = int(raw_input("Please enter second integer:"))
print "The sum of %d and %d is: %d" % (num1, num2, num1 + num2)
print "The difference between %d and %d is: %d" % (num1, num2, num1-num2)
print "The product of %d and %d is: %d" % (num1, num2, num1*num2)
print "The quotient of %d and %d is: %d" % (num1, num2, num1/num2),
print "With remainder of: %d" % (num1 % num2)