def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    count = count_words(text)
    print(f"Found {count} total words")

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()

    return text

def count_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    main()
