def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_freq(text):
    freqs = {}

    for char in text:
        if char.lower() not in freqs:
            freqs[char.lower()] = 1
        else:
            freqs[char.lower()] += 1

    return freqs

def get_char_table(freqs):
    table = []

    for char in freqs:
        char_dict = {}
        char_dict["char"] = char
        char_dict["num"] = freqs[char]
        table.append(char_dict)

    table.sort(key=lambda x: x["num"], reverse=True)

    return table