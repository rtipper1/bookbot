from stats import get_num_words, get_char_freq

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents



def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    freqs = get_char_freq(text)

    print(f"{num_words} words found in the document")
    print(freqs)


main()