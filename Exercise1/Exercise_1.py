num1 = raw_input("Please enter first integer: ")
while not num1.isdigit():
    num1 = raw_input("That in not a number. Please enter first integer: ")
num2 = raw_input("Please enter second integer:")
while not num2.isdigit() or int(num2) == 0:
    num2 = raw_input("Numbers only and not zero. Please enter second integer: ")


num1 = int(num1)
num2 = int(num2)
add = num1 + num2
sub = num1 - num2
prod = num1 * num2
quot = num1 / num2
remain = num1 % num2


print "The sum of %i and %i is: %i" % (num1, num2, add)
print "The difference between %i and %i is: %i" % (num1, num2, sub)
print "The product of %i and %i is: %i" % (num1, num2, prod)
print "The quotient of %i and %i is: %i With remainder of: %i" % (num1, num2, quot, remain)

