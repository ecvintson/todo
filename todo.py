import pickle

# Will be a program for writing to-do lists. Will save lists in a pickle file, and 
# pull them back out


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

def printList():
	print theList

def remList():


#library of commands, calling functions
commands = {
	'hello': helloWorld,
	'list': printList,
	'add': addList,
	'remove': remList,
	'save': 4,
	'quit': quitCommand
}




print "To Do List 0.2"


while True:
	uComm= raw_input()
	commands[uComm]()