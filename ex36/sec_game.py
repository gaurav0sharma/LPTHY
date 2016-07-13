import random

#---------------------Take team from the user---------------

def take_team():
	team_one=raw_input("please enter team one")
	team_two=raw_input("please enter team two")
	if team_one == team_two:
		print "Enter diffrant team man."
		exit(1)
	team_list=[team_one,team_two]
	return team_list

#-----------------Toss between the team---------------------

def Team_toss(team_one,team_two):
	i = random.random()
	i *= 10
	team_flag= int( i % 2 )
	print "%s" %  team_flag

	if( team_flag == 1 ):
		toss_winner=team_one
	else:
		toss_winner=team_two

	return toss_winner
	
#------------------Call the function. :) --------------------

def playteam():
	i = 1
	total_run = 0
	while(i<12):
		print "Please enter player",i,"run"
		run = input("> ")
		total_run += run
		i += 1
	print "total run %d" % total_run
	return total_run		


#---------------  Play Team-----------------------------------
team_one,team_two=take_team()


toss_winner_team=Team_toss(team_one,team_two)


print "Winner team is ",toss_winner_team

print "###### Team %s Playing ##########" % toss_winner_team

toss_winner_team_run= playteam()

print "#################################"

if team_one == toss_winner_team:
	other_team = team_two
else:
	other_team = team_one

print "###### Team %s Playing ##########" % other_team
other_team_run = playteam()

print "#################################"
print "toss_winnerTeamRum = %d" % toss_winner_team_run
print "other team Run = %d" % other_team_run

if toss_winner_team_run > other_team_run:
	print "********Winner**************"
	print "*    ",toss_winner_team,"      *"
	print "****************************"
elif toss_winner_team_run == other_team_run:
	print "*****************************"
	print "*        Tied               *"
	print "*****************************"
else:
	print "********Winner**************"
	print "*    ",other_team,"            *"
	print "****************************"

#print team_one
#print team_two
