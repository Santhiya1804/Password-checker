import itertools
import re
import os

def leetspeak(word):
    replacements = {'a': '@', 'i': '1', 'e': '3', 'o': '0', 's': '$'}
    return ''.join([replacements.get(c.lower(), c) for c in word])

def generate_variants(inputs):
    patterns = []
    for word in inputs:
        word = word.lower()
        patterns.extend([
            word,
            word.capitalize(),
            word + '123',
            word + '2025',
            leetspeak(word),
            leetspeak(word) + '2025'
        ])
    return list(set(patterns))


def save_wordlist(wordlist, filename="wordlists/custom_wordlist.txt"):
    # ✅ Ensure the folder exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(word + '\n')
    return filename
