# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Sidd Tewari

# Think Python 
# 8.3 (Pg 94 of 240)

import string

def fruitSpell(fruit):
	index = 0
	while index < len(fruit):
		print fruit[index]
		index = index + 1

# Exercise 8.1
def fruitBackward(fruit):
	counter = 0
	l = len(fruit)
	while counter < l:
		print fruit[l-1]
		l = l-1

def forFruit(fruit):
	for char in fruit:
		print char

#Exercise 8.2
def ducklings():
	prefixes = 'JKLMNOPQ'
	suffix ='ack'
	for letter in prefixes:
		if((letter == 'O') or (letter =='Q')):
			print letter + 'u' + suffix
		else:
			print letter + suffix

def slicedString():
	fruit = 'banana'
	print fruit[3:3]
	print fruit[:]

def find(word,letter,start):
	index = start

	while  index < len(word):
		if word[index] == letter: #print 'woohoo at', index
			return index
		index = index + 1     #print index #print 'woompa'
	return -1

def count(word, letter, start):
	countet = 0
	index = find(word, letter, start)

	if index == -1:
		countet = 0
	else:
		while index > -1:
			countet = countet + 1
			index = index + 1
			index = find(word, letter, index)
	print countet

def is_reverse(word1, word2):
	if len(word1) != len(word2):
		return False
	
	i = 0
	j = len(word2)-1

	while j >= 0:
		print i, j
		if word1[i] != word2[j]:
			return False
		i = i+1
		j = j-1
	print True
	return True



def rotNum(word, rot):
	""" Rotates a letter/word by n places. 
	This function is not fully functional for all cases
	For instance it gives special characters for letters closer to Z
	"""
	rottenString = ''
	#print len(word)

	for c in word:
		rotN = ord(c)
		rotIt = rotN + rot
		rottenW = chr(rotIt)
		rottenString += rottenW
	
	return rottenString
	#print rottenString

if __name__ == '__main__':
	print (rotNum('cheer', 7))
	print (rotNum('melon', -10))
	print (rotNum('sleep', 9)) 



def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    #print ord(letter)

    if letter.isupper():
        start = ord('A')
        #print start
    elif letter.islower():
        start = ord('a')
        #print start
    else:
        return letter

    x = ord(letter) - start
    #print x

    y = (x + n) % 26 + start
    #print i

    return chr(y)

def rotate_word(word, n):
	""" Rotates a word by n places

	word: string
	n: integer

	Returns: string
	"""
	res = ''
	for letter in word:
		res += rotate_letter(letter, n)
	return res

if __name__ == '__main__':
	print rotate_word('cheer', 7)
	print rotate_word('melon', -10)
	print rotate_word('sleep', 9)


#rotNum('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',0)

# fruitSpell('banana')
# fruitBackward('banana')
# forFruit('APPLE')
# ducklings()
# slicedString()
# find('Incognito', 'c', 0)
# count ('banana','a', 0)
# count ('apple', 'p', 0)
# count ('guvava', 'a', 0)
# count ('banana', 'a', 4)
# is_reverse('pots', 'stop')
# rotNum('Abc', 1)
# rotNum('sidd', 13)
# rotate_letter('a',0)
# rotate_letter('b',0)
# rotate_letter('c',0)
# rotate_letter('d',0)
# rotate_letter('b',0)

print 

