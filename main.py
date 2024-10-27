def main():
    book_path = "books/frankenstein.txt"
    bookText = get_book_text(book_path)
    word_count = get_words_count(bookText)
    char_dict = get_char_dict(bookText)
    report(char_dict, book_path, word_count)

def get_words_count(book):
    words = book.split()
    return len(words)

def get_char_dict(book):
    chars = {}

    for char in book:
        lowerCaseChar = char.lower()
        if(lowerCaseChar not in chars):
            chars[lowerCaseChar] = 1
        else:
            chars[lowerCaseChar] += 1

    return chars

def report(char_dict, path, word_count):
    print(f"--- Begin report of {path} ---\n")
    print(f"{word_count} words found in the document \n")
    print(f"--- Characters of the alphabet report ---\n")
    
    sorted_chars = list(char_dict.keys())
    sorted_chars.sort()
    
    for sc in sorted_chars:
        if not sc.isalpha():
            continue
        print(f"The character {sc} appeared {char_dict[sc]} times")
    
def get_book_text(path):
    with open(path) as book:
        return book.read()
    

main()