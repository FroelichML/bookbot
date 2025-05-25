def word_count (text_to_split):
	book_list = text_to_split.split()
	counter = 0
	for i in range (0,len(book_list)):
		counter += 1
	return counter

def letter_count (book_string):
	lowercase_text = book_string.lower()
	text_dict = {}

	for letter in lowercase_text:
		
		if letter in text_dict:
			text_dict[letter.lower()] = text_dict[letter.lower()] + 1
		else:
			text_dict[letter.lower()] = 1
	
	print (text_dict)