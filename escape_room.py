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

def najdi_start(mriezka):
    for r in range(len(mriezka)):
        for s in range(len(mriezka[r])):
            # ŠTART má bit 16 (číselná hodnota & 16 == 16)
            if mriezka[r][s] & 16:
                return r, s
    min_hodnota = float('inf')
    start_r, start_s = 0, 0
    for r in range(len(mriezka)):
        for s in range(len(mriezka[r])):
            if mriezka[r][s] < min_hodnota and mriezka[r][s] > 0:
                min_hodnota = mriezka[r][s]
                start_r, start_s = r, s
    return start_r, start_s


if __name__ == "__main__":
    labyrint = nacitaj_labyrint()
    print(f"Rozmery: {len(labyrint)}x{len(labyrint[0]) if labyrint else 0}")

    start_r, start_s = najdi_start(labyrint)
    print(f"ŠTART nájdený na pozícii: RIADOK {start_r}, STĹPEC {start_s}")
    print(f"Hodnota štartu: {labyrint[start_r][start_s]}")

    print("\nOkolie štartu:")
    for dr in [-1, 0, 1]:
        for ds in [-1, 0, 1]:
            nr, ns = start_r + dr, start_s + ds
            if 0 <= nr < len(labyrint) and 0 <= ns < len(labyrint[0]):
                print(f"  [{nr},{ns}]={labyrint[nr][ns]}", end=" ")
        print()