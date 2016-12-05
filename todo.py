import pickle

# Will be a program for writing to-do lists. Will save lists in a pickle file, and 
# pull them back out

def saveList():
	with open('save.pickle', 'wb') as handle:
		pickle.dump(todoList, handle)

def loadList():
	with open('save.pickle', 'rb') as handle:
		listLoad = pickle.load(handle)
		return listLoad
