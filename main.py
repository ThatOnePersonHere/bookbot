def get_book_info(location):
	from stats import get_num_words
	from stats import get_character_count
	book_location = location
	print(f'Analyzing book found at {location}...')
	get_num_words(book_location)
	get_character_count(book_location)
	print("============= END ===============")
	
def main():
	import sys
	try:
		book = sys.argv[1]
		program_info = "============ BOOKBOT ============"
		print(program_info)
		get_book_info(book)
	except Exception as e:
		print('Usage: python3 main.py <path_to_book>')
		sys.exit(1)

main()
