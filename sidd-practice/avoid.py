
# Ex 9.3

def avoid(word,forbidden):
	""" 
	Insert docstring

	"""
	for letter in word:
		if letter in forbidden:
			return False
	return True

def avoidThese():
	""" Insert docstring

	"""
	prompt = 'Please enter the forbidden characters: \n'
	letters = (raw_input(prompt)).strip()
	fin = open('words.txt')
	clearedWords = []
	numberOfWords = 0
	for line in fin:
		word = line.strip()
		if avoid(word,letters):
			numberOfWords = numberOfWords + 1
			clearedWords.append(word)
	print
	print 'Number of words = ', numberOfWords
	print
	return clearedWords

# def uses(word, required):
# 	for letter in required:
# 		if letter not in word:
# 			return False
# 		return True

# def atozCount():
# 	"""
# 	"""
# 	testList = ['a','b','c','d','e','f','g','h','i','z','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# 	resultList = []

# 	print len(testList)
# 	fin = open('words.txt')
	
# 	for line in fin:
# 		word = line.strip()
# 		while counter < len(testList):
# 			if uses(word,testList[counter]):
# 				numberOfWords = numberOfWords + 1
# 		letters = 
# 		if avoid(word,letters):

# if __name__ == '__main__':
# 	#avoidThese()
# 	atozCount()