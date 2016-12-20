import pickle

print "To Do List 0.9.0"

#variables
theList = []
global spltStr 
spltStr = []
global hasSplit
hasSplit = False

#pickle save/load functions
def saveList():
	with open('save.pickle', 'wb') as handle:
		pickle.dump(theList, handle)

def loadList():
	with open('save.pickle', 'rb') as handle:
		listLoad = pickle.load(handle)
		return listLoad



# Functions that are called by user inputs
def quitCommand():
	while True:
		print "Are you sure you want to quit? (y/n)"
		x = raw_input()
		if x == "y":
			saveCommand()
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
	x = len(theList)
	x = x-1
	i = 0
	while i<=x:
		y = str(i + 1)
		print (y + " " + theList[i])
		i = i +1


def remList():
	remint = raw_input()
	remint = int(remint)
	remint = remint - 1
	del theList[remint]

def helpCommand():
	tempList = commands.keys()
	tempStr = ""
	x = len(tempList)
	x = x-1
	i = 0
	while i<=x:
		y = str(i+1)
		tempStr =  (tempStr + tempList[i] + " ")
		i = i+1
		if i == 6:
			print tempStr


def saveCommand():
	saveList()

#library of commands, calling functions
commands = {
	'list': printList,
	'add': addList,
	'remove': remList,
	'save': saveCommand,
	'quit': quitCommand,
	'help': helpCommand
}


#attempts to load list, if save file does not exist, creates it
try:
	theList = loadList()
except IOError:
	saveList()

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