def read_text(path):
    """Läser text från en fil och returnerar som sträng."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
