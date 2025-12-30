from stats import count_words, get_char_frequencies, get_char_dicts


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    count = count_words(text)
    frequencies = get_char_frequencies(text)
    char_dicts = get_char_dicts(frequencies)
    print(char_dicts)
    print_report(filepath, count, frequencies)

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()

    return text

def print_report(filepath, word_count, char_frequencies):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

if __name__ == "__main__":
    main()
