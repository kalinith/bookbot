def main():
	bookpath = "books/frankenstein.txt"
	text = get_book_text(bookpath)
	num_words = word_count(text)
	print(f"{bookpath} contains {num_words} words.")
	char_dict = char_count(text.lower())
	print(char_dict)

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
			count = 0
		characters.update({char: count})
	return characters

main()
