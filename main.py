from stats import word_count
from stats import letter_count
from stats import sort_on


def get_book_text (path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	book_text = get_book_text("books/frankenstein.txt")
	
	print ("============ BOOKBOT ============")
	print ("Analyzing book found at books/frankenstein.txt...")
	print ("----------- Word Count ----------")
	print (f"Found {word_count(book_text)} total words")
	print ("--------- Character Count -------")
	letter_dict = letter_count(book_text)
	list_print = sort_on(letter_dict)
	for list in list_print:
		if list["char"].isalpha():
			print (f"{list["char"]}: {list["num"]}")
		else: 
			pass
	print ("============= END ===============")







	
	#book_text = get_book_text("books/frankenstein.txt")
	#book_wordcount = word_count(book_text)
	#print(f"{book_wordcount} words found in the document")
	#letter_dict = letter_count(book_text)
	#print (letter_dict)


main()
