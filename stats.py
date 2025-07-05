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
