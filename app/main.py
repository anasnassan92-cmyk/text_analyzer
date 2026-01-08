import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from analyzer.text_reader import read_text
from analyzer.text_processor import process_text
from analyzer.statistics import get_word_stats
from utils.logger import log_info, log_error
from utils.config import DATA_PATH

def main():
    try:
        log_info(f"Läser fil: {DATA_PATH}")
        text = read_text(DATA_PATH)
        words = process_text(text)
        stats = get_word_stats(words)

        log_info(f"Antal ord: {stats['count']}")
        log_info(f"Längsta ordet: {stats['longest']}")
        log_info("Mest förekommande ord:")
        for word, freq in stats['most_common']:
            print(f"{word}: {freq}")
    except Exception as e:
        log_error(f"Något gick fel: {e}")

if __name__ == "__main__":
    main()
