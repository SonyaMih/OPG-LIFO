def nacitaj_labyrint(soubor="labyrint.txt"):
    mriezka = []
    try:
        with open(soubor, 'r') as subor:
            for riadok in subor:
                riadok = riadok.strip()
                if riadok and not riadok[0].isdigit() and not riadok.startswith('Vysvetlivky'):
                    continue

                cela = []
                for x in riadok.split():
                    try:
                        cela.append(int(x))
                    except ValueError:
                        continue

                if cela:
                    mriezka.append(cela)
    except FileNotFoundError:
        print(f"CHYBA: Súbor {soubor} sa nenačítal!")
        return []

    return mriezka


if __name__ == "__main__":
    labyrint = nacitaj_labyrint()
    print("Labyrint načítaný:")
    print(f"Počet riadkov: {len(labyrint)}")
    if labyrint:
        print(f"Počet stĺpcov: {len(labyrint[0])}")
        print("Prvý riadok:", labyrint[0])
        print("Posledný riadok:", labyrint[-1])
    else:
        print("Žiadne dáta načítané!")
