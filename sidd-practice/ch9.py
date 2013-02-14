# fin = open('words.txt')
# #print fin

# for line in fin:
# 	word = line.strip()
# 	if len(word) > 20:
# 		print word

import string

# def noEallowed(word):
# 	for char in word:
# 		if char == 'e':
# 			return False
# 		else:
# 			return True

# if __name__ == '__main__':
# 	print noEallowed('gaby gillford')
# 	print noEallowed('eat')

def notAllowed(word, notAllowed):
	for har in word:
		for sny in notAllowed:
			if har == sny:
				return False
			else:
				return True

# def uses_only(word, forbidden):
# 	for char in forbidden:
# 		if wo
		
if __name__ == '__main__':
	print notAllowed('kabhi', 'a')


	