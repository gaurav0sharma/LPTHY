print "you enter a dark room with two doors.Do you go through door #1 or #2"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake.what do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")
	
	if bear == "1":
		print "the bear eats your face off. Good job!"
	elif bear == "2":
		print "the bear eats your legs off. Good job"
	else:
		print "Well,doing %s is probably better.bear runs away." % bear

elif door == "2":
	print "you stare into the endless abyss at cthulhu's retina."
	print "1. BlueBerrires"
	print "2. Yellow Jacket clothespins"
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good Job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good Job!"

else:
	print "You stumble around and fall on a knife and die. Good Job!"
