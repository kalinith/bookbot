def main():
	bookpath = "books/frankenstein.txt"
	text = get_book_text(bookpath)
	num_words = word_count(text)
	char_dict = char_count(text.lower())
	ordered_dict = dict_to_list(char_dict)
	ordered_dict.sort(reverse=True, key=sort_on)

	print(f"--- Begin report of {bookpath} ---")
	print(f"{num_words} of words found in the document.")
	print()
	print()
	print_wordcount(ordered_dict)
	print("--- End report ---")


def print_wordcount(characters):
	for item in characters:
		if item['char'].isalpha():
			print(f"The {item['char']} character was found {item['num']} times")

def dict_to_list(char_dict):
	list_of_dicts = []
	for char, num in char_dict.items():
		list_of_dicts.append({"char":char, "num":num})
	return list_of_dicts

def sort_on(dict):
    return dict["num"]


def word_count(file_contents):
	words = file_contents.split()
	return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def char_count(file_contents):
	characters = {}
	for i in range(0,len(file_contents)):
		char = file_contents[i]
		try:
			count = characters[f"{char}"] + 1
		except:
			count = 1
		characters.update({char: count})
	return characters

main()
