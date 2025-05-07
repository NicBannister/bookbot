from stats import num_of_words, convert_to_lower, character_frequency, sorted_dict
import sys


def get_book_text(bookpath):
    file_contents = bookpath.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path) as bookpath:
        book_contents = get_book_text(bookpath)
        word_count = num_of_words(book_contents)

        print("============ BOOKBOT ============")
        print("Analyzing book found at", file_path, "...")
        print("----------- Word Count ----------")
        print("Found", word_count, "total words")
        print("--------- Character Count -------")

        lowercase_contents = convert_to_lower(book_contents)

        char_freq = character_frequency(lowercase_contents)

        #print(char_freq)

        sorted_char_count = sorted_dict(char_freq)
        for item in sorted_char_count:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
             
        



main()