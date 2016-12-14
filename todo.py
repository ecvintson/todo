import pickle

print "To Do List 0.5.1"

#variables
theList = []
global spltStr 
spltStr = []
global hasSplit
hasSplit = False

#pickle save/load functions
def saveList():
	with open('save.pickle', 'wb') as handle:
		pickle.dump(todoList, handle)

def loadList():
	with open('save.pickle', 'rb') as handle:
		listLoad = pickle.load(handle)
		return listLoad



# Functions that are called by user inputs
def helloWorld():
	print "Hello World!!"

def quitCommand():
	while True:
		print "Are you sure you want to quit? (y/n)"
		x = raw_input()
		if x == "y":
			quit()
		elif x == "n":
			break
		else:
			print "Invalid input"	

def addList():
	if hasSplit == True:
		theList.append(spltStr[1])
		print theList

	else:
		x = raw_input()
		theList.append(x)


def printList():
	print theList

#will allow user to remove items from the list
def remList():
	pass

def helpCommand():
	#temporary, need to make look nicer
	print commands.keys()

#will save list 
def saveCommand():
	pass

#library of commands, calling functions
commands = {
	'hello': helloWorld,
	'list': printList,
	'add': addList,
	'remove': remList,
	'save': saveCommand,
	'quit': quitCommand,
	'help': helpCommand
}






#main loop
while True:
	spltStr = []
	uComm= raw_input()
	try:	
		if " " in uComm: #if user input a command, followed by some text
			spltStr = uComm.split(' ', 1) #split the command from the rest of the text into a list
			hasSplit = True
			commands[spltStr[0]]() #pass the command through the dictionary
			hasSplit = False
		else:
			commands[uComm]() #otherwise simply pass the input through the dictionary
	except KeyError:
		print ("'" + uComm + "'" + " is not a valid input. Type 'help' for a list of commands.")