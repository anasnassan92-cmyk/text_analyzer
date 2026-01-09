# app/main.py

from analyzer.text_reader import read_text
from analyzer.text_processor import count_words, longest_word, most_common_words

def spara_resultat(resultat, filnamn):
    """Spara resultatet i en textfil"""
    with open(filnamn, "w", encoding="utf-8") as f:
        f.write(f"Antal ord: {resultat['antal_ord']}\n")
        f.write(f"Längsta ordet: {resultat['langsta_ord']}\n")
        f.write("Mest förekommande ord:\n")
        for word, count in resultat['mest_forekommande'].items():
            f.write(f"{word}: {count}\n")
    print(f"[INFO] Resultatet sparat i {filnamn}")

def analysera_text(text):
    """Analysera text och returnera en dictionary med resultat"""
    return {
        "antal_ord": count_words(text),
        "langsta_ord": longest_word(text),
        "mest_forekommande": most_common_words(text)
    }

def huvudmeny():
    print("Hi 👋\nVälkommen till Textanalysatorn")

    while True:
        print("\nVälj hur du vill mata in text:")
        print("1 - Skriv in text manuellt")
        print("2 - Läs text från fil")
        val = input("Ditt val (1 eller 2): ")

        if val == "1":
            text = input("\nSkriv in din text:\n")
        elif val == "2":
            filnamn = input("\nAnge filnamn i data-mappen (ex: sample.txt): ")
            path = f"data/{filnamn}"
            text = read_text(path)
            if text == "":
                print("❌ Filen finns inte.")
                continue
        else:
            print("❌ Ogiltigt val.")
            continue

        resultat = analysera_text(text)

        print("\n[INFO] Resultat av analysen:")
        print(f"Antal ord: {resultat['antal_ord']}")
        print(f"Längsta ordet: {resultat['langsta_ord']}")
        print("[INFO] Mest förekommande ord:")
        for word, count in resultat['mest_forekommande'].items():
            print(f"{word}: {count}")

        spara = input("\nVill du spara resultatet i en fil? (ja/nej): ")
        if spara.lower() == "ja":
            spara_resultat(resultat, "resultat.txt")

        mer = input("\nVill du analysera en annan text eller fil? (ja/nej): ")
        if mer.lower() != "ja":
            print("\nProgrammet avslutas. Hej då 👋")
            break

if __name__ == "__main__":
    huvudmeny()
