from sys import argv

script, filename = argv

print "We are going to erase %r" % filename
print "If you don't want,hit CTRL-C (^C)."
print "If you do want that,hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate() #turncate function is use to empties file.

print "Now I'm goint to ask you for three lines."

line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")

print "I'm going to write these to the file."
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')


print "now m try to close the file."

target.close()

print "==" * 20
print "now i want to read new file"

target = open(filename, 'r')

print "==" * 10
print target.read()
print "==" * 10
print "close this file with the help of close function"
target.close()


print "==" * 20
print "now i want to append this file."

line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")
target = open(filename,'a')
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
print "==" * 20

target.close()

print "==" * 20
print "now i want to read new file"

target = open(filename, 'r')

print "==" * 10
print target.read()
print "==" * 10
print "close this file with the help of close function"
target.close()


