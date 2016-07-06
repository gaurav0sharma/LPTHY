def print_two(*args):
#	print argv
	arg1,arg2,arg3 = args
	print args
	print args[0]
	print "arg1: %r, arg2: %r, arg3: %r" % (arg1,arg2,arg3)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1,arg2)

def print_one(arg1):	
	print "arg1: %r" % arg1

def print_none():
	print "none function."

print_two("zed","shaw","pagal")
print_two_again("zed","shaw")
print_one("zed")
print_none()
