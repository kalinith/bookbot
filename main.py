import sys
from stats import word_count, print_wordcount

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	bookpath = sys.argv[1]
	text = get_book_text(bookpath)
	num_words = word_count(text)
	char_dict = char_count(text.lower())
	ordered_dict = dict_to_list(char_dict)
	ordered_dict.sort(reverse=True, key=sort_on)

	print(f"============ BOOKBOT ============")
	print(f"Analyzing book found at {bookpath}...")
	print(f"----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print(f"--------- Character Count -------")
	print()
	print_wordcount(ordered_dict)
	print("============= END ===============")


def dict_to_list(char_dict):
	list_of_dicts = []
	for char, num in char_dict.items():
		list_of_dicts.append({"char":char, "num":num})
	return list_of_dicts

def sort_on(dict):
    return dict["num"]

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
