def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    words_list = text.split()
    count = word_count(words_list)
    char_dict = count_characters(text)
    list_of_dicts = dict_to_sorted_list(char_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} number of words in document")
    print()

    for dict in list_of_dicts:
        print(f"The '{dict["char"]}' character was found {dict["num"]} of times.")
    
    print("--- End report ---")


def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(dict):
    list = []
    for key in dict:
        if key.isalpha():
            list.append({"char": key, "num": dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list


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
