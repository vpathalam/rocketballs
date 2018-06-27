#!/usr/bin/python

import sys
from datetime import date

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
		date_string = str(date.today())
		with open(PLAYERS_PATH + name, 'a') as file:
			file.write('\n' + date_string) 
	else:
		print("You have to set your name before registering a hit")





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
	else:
		#No command given, print short help message
		default_message()
