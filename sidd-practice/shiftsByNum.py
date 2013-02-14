import string

def shiftsLetterByNum(letter,n):
	"""Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
	"""

	# all this entire if loop is doing is assigning an 
	# appropriate value to start based on the case of the letter
	if letter.isupper():
		# this assigns the number value of capital A to start
		start = ord('A')    
	elif letter.islower():
		# the numeric value of small a to start if the letter passed 
		# is lowercase
		start = ord('a')
	else:
		return letter

	# this statement? expression? bring it to 1,2,3 sequence
	x = ord(letter) - start

	# this statement adds the requested rotation number 
	# to shift the letter by and adds it to the 0 - 26 ranking
	y = (x + n) % 26 + start

	# this returns the actual result - the rotated value letter by letter
	return chr(y)


def shiftsWordByNum(word, n):
	""" Rotates a word by n places.  

	word: string
	n: integer

	Returns: string
	"""
	res = ''
	for poop in word:
		res += shiftsLetterByNum(poop, n)
	return res
	

if __name__ == '__main__':
	print
	print (shiftsWordByNum('cheer', 7))
	print (shiftsWordByNum('melon', -10))
	print (shiftsWordByNum('sleep', 9))    
	print (shiftsWordByNum('ZZ TOP', 500)) 
	print