from stats import num_of_words, convert_to_lower, character_frequency

def get_book_text(bookpath):
    file_contents = bookpath.read()
    return file_contents


def main():
    with open("/home/nicb/Documents/bookbot/books/frankenstein.txt") as bookpath:
        book_contents = get_book_text(bookpath)
        word_count = num_of_words(book_contents)

        print(word_count, "words found in the document")

        lowercase_contents = convert_to_lower(book_contents)

        char_freq = character_frequency(lowercase_contents)

        print(char_freq)

        #formatted = '{' + ','.join(f"'{k}':{v}" for k, v in char_freq.items()) + '}'
        #print(formatted)
       
        
        #for key in char_freq:
            #print(key, ":", char_freq[key])
           
        



main()