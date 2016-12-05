import pickle


def saveList():
	with open('save.pickle', 'wb') as handle:
		pickle.dump(todoList, handle)

def loadList():
	with open('save.pickle', 'rb') as handle:
		listLoad = pickle.load(handle)
		return listLoad
