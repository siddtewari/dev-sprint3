# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Sidd Tewari

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
	#traverse using FOR loop
	for letter in word:
		if letter == 'e':
			return False
	return True

def noEallowed(word):
	#traverse using WHILE loop
	index = 0
	while index < len(word):
		if word[index] == 'e':
			return False #"Its got e"
		index = index + 1
	return "Its E Free"

# Ex 9.3
def avoid(word,forbidden):
	""" 
	Insert docstring

	"""
	for letter in word:
		if letter in forbidden:
			return False
	return True

# Ex 9.3 Part II
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

# Ex 9.4
def uses_only(word, available):
	for letter in word:
		if letter not in available:
			return False
		return True

# --------------------------------------

def uses_all(word, required):
	for letter in required:
		if letter not in word:
			return False
		return True

# Can you make a sentence using only 
# the letters acefhlo? Other than Hoe alfalfa

if __name__ == '__main__':
	# longWords()

	# print noEallowed('gaby gillford')
	# print noEallowed('beat')

	# print avoids('sidd','exd')
	# print avoids('hammer', 'xyz')

	print avoidThese()

	print uses_only('Sidd', 'sidd ')



