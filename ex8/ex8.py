#ptining 
formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,True,False)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % ("this is string one","String Two","string three","string four")
#print "%d %d" % True,False
#above line give error TypeError: not enough arguments for format string

