def bear_room():
	print "There is a bear here"
	print "the bear has a bunch of honey"
	print "the fat bear is in front of another door"
	print "How are you going to move the bear?"
	bear_moved = False
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("the bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "the bear has moved from the door. you can go through it"
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("the bear gets pissed off and chews you leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
			print "this is gold room block"
		else:
			print "I got no idea what that means."

#------------------------------------------------------
def dead(why):
	print why, "Good Job!"
	exit(0)

#------------------------------------------------------
def gold_room():
	print "this is full of gold. how much do you take."
	
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, You're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
#------------------------------------------------------
def cthulhu_room():
	print "Here you see the great evil Cthulhu"
	print "He, it ,whatever starts at you and you go insane."
	print "Do you flee for your life or eat your head"
	
	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty")
	else:
		cthulhu_room()

#------------------------------------------------------
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
		print "this is bear room"
	elif choice == "right":
		cthulhu_room()
		print "this is cthulhu room"
	else:
		dead("are you mad man....?")

#------------------------------------------------------
start()
print "hello after if-else"
