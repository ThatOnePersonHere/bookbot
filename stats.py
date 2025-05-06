## Hello World!!
def get_num_words(location):
	selected_book = location
	print("----------- Word Count ----------")
	with open(selected_book) as book:
		book_contents = book.read()
		book_contents_word_count = len(book_contents.split())
		print(f'Found {book_contents_word_count} total words')

def print_out_dict(dictonary):
	for key in dictonary:
		if key.isalpha():
			print(f'{key}: {dictonary[key]}')

def get_character_count(location):
	selected_book = location
	character_count = {}
	print('--------- Character Count -------')
	with open(selected_book) as book:
		book_contents = book.read()
		book_lower = book_contents.lower()
	book_words = book_lower.split()
	for word in book_words:
		for letter in word:
			if letter in character_count:
				character_count[letter] += 1
			else:
				character_count.update({letter : 1})
	character_count = dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))
	#character_count.sort(reverse=True, key="num")	
	print_out_dict(character_count)
