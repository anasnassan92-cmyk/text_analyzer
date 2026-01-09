from collections import Counter

def count_words(text):
    return len(text.split())

def longest_word(text):
    words = text.split()
    return max(words, key=len) if words else ""

def most_common_words(text):
    words = text.lower().split()
    counts = Counter(words)
    return dict(counts.most_common(5))  # top 5 words
