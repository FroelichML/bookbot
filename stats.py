def word_count (text_to_split):
	book_list = text_to_split.split()
	counter = 0
	for i in range (0,len(book_list)):
		counter += 1
	return counter