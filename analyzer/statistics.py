# analyzer/statistics.py

from collections import Counter

def print_statistics(words):
    """Skriver ut statistik för orden"""
    print("[INFO] Mest förekommande ord:")
    word_counts = Counter(words)
    for word, count in word_counts.most_common(5):
        print(f"{word}: {count}")
