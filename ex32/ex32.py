the_count = [1,2,3,4,5,6,7,8,9,0]
fruits = ['apple','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
	print "this is count %d" % number

for fruit in fruits:
	print "a fruit of types: %s" % fruit

for i in change:
	print "i got %r" % i
	print type(i)

elements = []

for i in range(0,6):
	print i
	elements.append(i)

for i in elements:	
	print "element was: %d" % i
