import re

def process_text(text):
    """Rensar text och returnerar lista med ord."""
    # Ta bort skiljetecken
    text = re.sub(r"[^\w\s]", "", text)
    # Dela texten i ord
    words = text.lower().split()
    return words
