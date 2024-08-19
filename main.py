def main():
	bookpath = "books/frankenstein.txt"
	text = get_book_text(bookpath)
	num_words = word_count(text)
	print(f"{bookpath} contains {num_words} words.")


def word_count(file_contents):
	words = file_contents.split()
	return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
