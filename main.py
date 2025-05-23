def get_book_text (path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def word_count (text_to_split):
	book_list = text_to_split.split()
	counter = 0
	for i in range (0,len(book_list)):
		counter += 1
	return counter
	

def main():
	book_text = get_book_text("books/frankenstein.txt")
	book_wordcount = word_count(book_text)
	print(f"{book_wordcount} words found in the document")

main()
