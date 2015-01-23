def open_file(a_file):
	with open(a_file, "r") as f:
		pass


def open_file2(a_file):
	try:
		with open(a_file, "r") as g:
			pass

	except IOError:
		print "IOError exception has been handled"


try:
	open_file("exercise6.txt")
except IOError:
	print"IOError exception has been handled"

open_file2("exercise6.txt")