import string

# Ex 9.1
def longWords():
	fin = open('words.txt')
	#print fin
	for line in fin:
		word = line.strip()
		if len(word) > 20:
			print word

# Ex 9.2
def has_no_e(word):
	#traverse using for loop
	for letter in word:
		if letter == 'e':
			return False
	return True

def noEallowed(word):
	#traverse using while loop
	index = 0
	while index < len(word):
		if word[index] == 'e':
			return "Its got e"
		index = index + 1
	return "Its E Free"

# Ex 9.3
# More generalized version of noEAllowed
def avoid(word,forbidden):
	""" takes two arguements and passes on each forbidden character to 
	the noXAllowed function to check if the word has any

	word: 
	letters:

	"""
	for letter in word:
		if letter in forbidden:
			return False
	return word

# def avoids(word, letters):
	
# 	index = 0
# 	while index < len(letters):
# 		result = noXAllowed(word, letters[index])
# 		index = index + 1
# 	return result

# Ex 9.3 Part II
def avoidThese():
	prompt = 'Please enter the forbidden characters: \n'
	letters = (raw_input(prompt)).strip()
	fin = open('words.txt')
	counter = 0
	clearedWords = []
	for line in fin:
		word = line.strip()
		print avoid(word,letters)
		clearedWords[counter] = avoid(word,letters)
		#print word, letters
		counter = counter + 1
	print clearedWords

if __name__ == '__main__':
	# longWords()

	# print noEallowed('gaby gillford')
	# print noEallowed('beat')

	# print avoids('sidd','exd')
	# print avoids('hammer', 'xyz')

	avoidThese()




	