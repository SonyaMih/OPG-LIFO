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

def ma_dvere(bunka, smer):
    if smer == 'S': return bunka & 1  # Sever = 1
    if smer == 'V': return bunka & 2  # Vychod = 2
    if smer == 'J': return bunka & 4  # Juh = 4
    if smer == 'Z': return bunka & 8  # Zapad = 8
    return False

def posun_pozicia(r, s, smer):
    if smer == 'S': return r-1, s
    if smer == 'V': return r, s+1
    if smer == 'J': return r+1, s
    if smer == 'Z': return r, s-1
    return None

def zoznam_dveri(mriezka, r, s):
    dvere = []
    if ma_dvere(mriezka[r][s], 'S'): dvere.append('SEVER')
    if ma_dvere(mriezka[r][s], 'V'): dvere.append('VYCHOD')
    if ma_dvere(mriezka[r][s], 'J'): dvere.append('JUH')
    if ma_dvere(mriezka[r][s], 'Z'): dvere.append('ZAPAD')
    return dvere


if __name__ == "__main__":
    labyrint = nacitaj_labyrint()
    print(f"Rozmery: {len(labyrint)}x{len(labyrint[0]) if labyrint else 0}")

    start_r, start_s = najdi_start(labyrint)
    print(f"ŠTART nájdený na pozícii: RIADOK {start_r}, STĹPEC {start_s}")
    print(f"Hodnota štartu: {labyrint[start_r][start_s]}")

    dostupne = zoznam_dveri(labyrint, start_r, start_s)
    print(f"V štarte máš dvere: {', '.join(dostupne) if dostupne else 'Žiadne'}")
    print(f"Číselná hodnota štartu: {labyrint[start_r][start_s]}")