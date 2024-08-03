def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    words_list = text.split()
    print(word_count(words_list))
    print(count_characters(text))


def word_count(words_list):
    count = len(words_list)
    return count


def count_characters(book_string):
    character_dict = {}
    lowered_string = book_string.lower()
    for char in lowered_string:
        if char not in character_dict:
            character_dict[char] = lowered_string.count(char)
    return character_dict


def get_book_path(path):
    with open(path) as f:
        return f.read()


main()
