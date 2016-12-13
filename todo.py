import pickle


#pickle save/load functions
def saveList():
	with open('save.pickle', 'wb') as handle:
		pickle.dump(todoList, handle)

def loadList():
	with open('save.pickle', 'rb') as handle:
		listLoad = pickle.load(handle)
		return listLoad

#list to hold To Do items
theList = ["first", "second"]

# Functions that are called by user inputs
def helloWorld():
	print "Hello World!!"

def quitCommand():
	quit()	

def addList():
	x = raw_input()
	theList.append(x)
	print theList

def printList():
	print theList

def remList():
	print "placeholder"

def helpCommand():
	#temporary, fix
	print commands

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




print "To Do List 0.2.1"

#main loop
while True:
	uComm= raw_input()
	commands[uComm]()