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
	
	return text_dict

def sort_value (value):
	return value["num"]

def sort_on (passed_dict):
	
	dict_list = []
	for letter in passed_dict:
		temp_dict= {}
		temp_dict ["char"] = letter
		temp_dict ["num"] = passed_dict[letter]
		dict_list.append(temp_dict)
	dict_list.sort(reverse=True, key=sort_value )
	return dict_list
