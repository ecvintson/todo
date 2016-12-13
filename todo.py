import pickle

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
		hasSplit == False
	else:
		x = raw_input()
		theList.append(x)


def printList():
	print theList

def remList():
	pass

def helpCommand():
	#temporary, need to make look nicer
	print commands.keys()

def saveCommand():
	pass

#library of commands, calling functions
commands = {
	'hello': helloWorld,
	'list': printList,
	'add': addList,
	'remove': remList,
	'save': 4,
	'quit': quitCommand,
	'help': helpCommand
}





#main loop
while True:
	uComm= raw_input()
	
	if " " in uComm:
		spltStr = uComm.split(' ', 1)
		hasSplit = True
		commands[spltStr[0]]()

	else:
		commands[uComm]()
	# add loop to check to make sure input matches a command 
	# (or add a default functionality in dictionary?)
