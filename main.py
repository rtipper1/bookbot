from stats import get_num_words, get_char_freq, get_char_table
import sys

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents

def print_report(filepath, num_words, char_table):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char in char_table:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    freqs = get_char_freq(text)
    char_table = get_char_table(freqs)

    print(f"{num_words} words found in the document")
    print_report(filepath, num_words, char_table)


main()