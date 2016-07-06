def add(a,b):	
	print "Adding %d + %d" % (a, b)
	return a + b

def sub(a,b):
	print "Subtracting %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "multipling %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "divinding %d / %d" % (a, b)
	return a / b

print "Let's do some math with just function!"

age = add(20, 2)
height = sub (8, 2)
weight = multiply(90, 2 )
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."

what = add(age,sub(height,multiply(weight,divide(iq,2))))

print "that become:", what, "Can you do it by hand?"

print (2+ -3)
