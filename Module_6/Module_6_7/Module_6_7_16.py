from collections import Counter


def count_occurences(word, words):
    return Counter([w.lower() for w in words.split()])[word.lower()]
