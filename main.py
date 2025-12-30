import sys
from stats import count_words, get_char_frequencies, get_char_dicts


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    count = count_words(text)
    frequencies = get_char_frequencies(text)
    char_dicts = get_char_dicts(frequencies)
    print_report(filepath, count, char_dicts)

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()

    return text

def print_report(filepath, word_count, char_dicts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in char_dicts:
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
