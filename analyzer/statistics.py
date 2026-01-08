from collections import Counter

def get_word_stats(words):
    """Returnerar statistik om orden i texten."""
    count = len(words)
    longest = max(words, key=len) if words else ""
    most_common = Counter(words).most_common(5)
    
    return {
        "count": count,
        "longest": longest,
        "most_common": most_common
    }
