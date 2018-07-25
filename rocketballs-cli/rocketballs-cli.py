#!/usr/bin/python

import sys
import datetime
import os

PLAYERS_PATH = '../players/' #Path to players directory


#Print a default message if no valid command is given
def default_message():
	print("Rocketballs CLI:\nType 'python rocketballs-cli.py help' for help")
	

#Save name to config file
def set_name(name):
	with open('config', 'w') as file:
		file.write(name)

def get_name():
	with open('config', 'r') as file:
		return file.read()
	return ''


#Register a hit
def hit():
	name = get_name()
	if len(name) > 0:
		date_string = str(datetime.datetime.utcnow())
		with open(PLAYERS_PATH + name, 'a') as file:
			file.write('\n' + date_string) 
	else:
		print("You have to set your name before registering a hit")

#Returns a list of the players names
def get_players():
	to_return = []
	for root, dirs, files in os.walk(PLAYERS_PATH):  
		for filename in files:
			to_return.append(str(filename))
	return to_return

#Returns a list of each line of a player's data file
def get_player_data(player_name):
	with open(PLAYERS_PATH + player_name, 'r') as file:
		player_data = file.read()
		return player_data.split("\n")
			
	return []

#Print each player and their hit count
def print_counts():
	for player_name in get_players():
		print(player_name + ": " + str(len(get_player_data(player_name))))



#Get the command line arguments
cli_arguments = sys.argv

#If no command is given print the default message
if(len(cli_arguments) < 2):
	default_message()
else:
	command_argument = cli_arguments[1]
	
	#Perform the action specified by command_argument
	if command_argument == 'help':
		#Print contents of README
		with open('README', 'r') as file:
			print(file.read())
	elif command_argument == 'hit':
		hit()	
	elif command_argument == 'set-name':
		#Write name to config file
		if(len(cli_arguments) >= 3):
			set_name(cli_arguments[2])
		else:
			print('No name given\nCorrect set-name usage: python rocketballs-cli.py set-name <your first name>')
	elif command_argument == "count":
		print_counts()
	else:
		#No command given, print short help message
		default_message()
