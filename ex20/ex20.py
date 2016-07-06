from sys import argv
script,input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)   #pointer move to start of the file.
	#f.seek(1)	#pointer move one byte it's print 'aurav' instead of 'gaurav'
def print_a_line(line_count,f):
	print line_count,f.readline()

current_file = open(input_file)

print "first let's print the whole file:\n"
print_all(current_file)

print "==" * 20

print "Now let's rewind, kind of like a tape."

rewind(current_file)
print "Now let's print three lines:\n"
current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)
current_line = current_line + 1
print_a_line(current_line,current_file)
