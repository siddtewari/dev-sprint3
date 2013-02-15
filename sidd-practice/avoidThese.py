# Ex 9.3 Part II
def noXAllowed(word,letter):
	index = 0
	result = ''
	while index < len(word):
		if word[index] == letter:
			result = False
		index = index + 1
	result = True
	return result

def avoids(word, letters):
	""" takes two arguements and passes on each forbidden character to 
	the noXAllowed function to check if the word has any

	word: 
	letters:

	"""
	index = 0
	while index < len(letters):
		result = noXAllowed(word, letters[index])
		index = index + 1
	return result


def avoidThese():
	prompt = 'Please enter the forbidden characters: \n'
	letters = raw_input(prompt)

	#letters = inp.strip
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		listem = avoids(word,letters)
	print listem

if __name__ == '__main__':
	# longWords()

	# print noEallowed('gaby gillford')
	# print noEallowed('beat')

	# print avoids('sidd','exd')
	# print avoids('hammer', 'xyz')

	avoidThese()