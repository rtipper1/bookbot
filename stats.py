def count_words(text):
    words = text.split()
    return len(words)

def get_char_frequencies(text):
    frequencies = {}

    for char in text:
        if char.isalpha():
            if char.lower() not in frequencies:
                frequencies[char.lower()] = 1

            else:
                frequencies[char.lower()] += 1

    return frequencies

def get_char_dicts(frequencies):
    dicts = []
    for key, value in frequencies.items():
        char_dict = {}
        char_dict["char"] = key
        char_dict["num"] = value
        dicts.append(char_dict)

    def sort_on(dicts):
        return dicts["num"]

    dicts.sort(reverse=True, key=sort_on)

    return dicts
