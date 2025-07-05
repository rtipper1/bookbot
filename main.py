from stats import get_num_words, get_char_freq, get_char_table

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents



def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    freqs = get_char_freq(text)
    char_table = get_char_table(freqs)

    print(f"{num_words} words found in the document")
    print(char_table)


main()