from collections import Counter


def scrabble(symbols, word):
    symbols = Counter(symbols.lower())
    word = Counter(word.lower())
    for k in word:
        if symbols[k] < word[k]:
            return False
    return True
