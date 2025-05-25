from stats import word_count
from stats import letter_count

def get_book_text (path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	book_text = get_book_text("books/frankenstein.txt")
	book_wordcount = word_count(book_text)
	print(f"{book_wordcount} words found in the document")
	letter_dict = letter_count(book_text)
	print (letter_dict)
main()
