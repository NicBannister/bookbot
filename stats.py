
def num_of_words(book_contents):
    word_count = len(book_contents.split())
    return word_count

def convert_to_lower(book_contents):
    lowercase = book_contents.lower()
    return lowercase

def character_frequency(book_contents):
    char_dict = {}

    for line in book_contents:
        for char in line:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

    return char_dict


def sorted_dict(char_count):
    sorted_char_list = []

    for char,count in char_count.items():
        if char.isalpha():
            sorted_char_list.append(({'char': char, 'num': count}))
    sorted_char_list.sort(key=lambda x: x["num"], reverse=True)

    return sorted_char_list

