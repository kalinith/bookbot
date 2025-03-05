def word_count(file_contents):
        words = file_contents.split()
        return len(words)

def print_wordcount(characters):
        for item in characters:
                if item['char'].isalpha():
                        print(f"{item['char']}: {item['num']}")
