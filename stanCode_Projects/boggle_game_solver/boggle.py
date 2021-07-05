"""
File: boggle.py
Name: Jael Lin
----------------------------------------
TODO: This program recursively finds all the word(s) for 16 letters input by user.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
d = []
new_d1 = []
new_d2 = []
new_d3 = []


def main():
	"""
	:param : (str) 16 letters on a 4x4 square grid
	:return: All the word(s) find from the dictionary
	"""
	read_dictionary()

	count = 0
	word_list = []
	for i in range(4):
		row = input(str(i+1) + " row of letters: ")
		count += 1
		if illegal_input(row):
			print("Illegal input")
			break
		row = row.lower()
		row = row.split()
		for alpha in row:
			word_list.append(alpha)

	if count == 4:
		start = time.time()
		ans = []
		find_words(word_list, ans)
		end = time.time()

		for answer in ans:
			print(f'Found {answer}')
		print(f'There are \"{len(ans)}\" words in total.')
		print('----------------------------------')
		print(f'The speed of your anagram algorithm: {end - start} seconds.')


def find_words(word_list, ans):
	for x in range(4):
		for y in range(4):
			location = []
			first_alpha = word_list[x+4*y]
			first_location = (x, y)
			location.append(first_location)
			word = first_alpha
			if has_prefix(word):
				find_words_helper(word_list, word, ans, first_location, location)


def find_words_helper(word_list, word, ans, first_location, location):
	if len(word) >= 4:
		if word in d and word not in ans:
			ans.append(word)

	for j in range(-1, 2, 1):
		for i in range(-1, 2, 1):
			if 0 <= (first_location[0]+i) < 4:
				if 0 <= (first_location[1]+j) < 4:
					if i != 0 or j != 0:
						if (first_location[0]+i, first_location[1]+j) not in location:
							next_alpha = word_list[(first_location[0]+i)+4*(first_location[1]+j)]
							word += next_alpha
							first_location = (first_location[0]+i, first_location[1]+j)
							location.append(first_location)
							if has_prefix(word):
								find_words_helper(word_list, word, ans, first_location, location)
							word = word[0:len(word)-1]
							location.pop(-1)
							first_location = (first_location[0] - i, first_location[1] - j)


def illegal_input(row):
	if len(row) != 7:
		return True
	for i in range(7):
		if i % 2 == 0:
			if not row[i].isalpha():
				return True
		if i % 2 == 1:
			if row[i] != " ":
				return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, "r")as f:
		for line in f:
			line = line.strip()
			d.append(line)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	if len(sub_s) == 1:
		for word in d:
			if word.startswith(sub_s):
				new_d1.append(word)
		return True
	elif len(sub_s) == 2:
		for word in new_d1:
			if word.startswith(sub_s):
				new_d2.append(word)
		return True
	elif len(sub_s) == 3:
		for word in new_d2:
			if word.startswith(sub_s):
				new_d3.append(word)
		return True
	else:
		for word in new_d3:
			if word.startswith(sub_s):
				return True


if __name__ == '__main__':
	main()
