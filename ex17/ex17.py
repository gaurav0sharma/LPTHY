from sys import argv
from os.path import exists

script, from_file,to_file =argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "the input file is %d bytes long" % len(indata) #print the size of string

print "Does the output file exist?" * exists(to_file)
print "Ready, hit RETURN to continue??"
raw_input()
out_file = open(to_file,'w')
out_file.write(indata)
print "alright,all done"
out_file.close()
in_file.close()
