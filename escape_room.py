import time

class myStack:
    def __init__(self, capacity):
        if capacity <= 0: raise ValueError("Kapacita > 0")
        self.top = 0
        self.capacity = capacity
        self.buffer = [None] * capacity

    def push(self, smer):
        if self.top == self.capacity: raise OverflowError("Stack overflow")
        self.buffer[self.top] = smer
        self.top += 1

    def pop(self):
        if self.top == 0: raise IndexError("Stack prázdny")
        self.top -= 1
        return self.buffer[self.top]

    def freeCap(self):
        return self.capacity - self.top

    def clear(self):
        self.top = 0

    def toString(self):
        return str(self.buffer[:self.top])

    def see(self):
        smery = self.buffer[:self.top]
        if smery:
            return " <- ".join(smery)
        return "Prázdny"

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

def posun_pozicia(r, s, prikaz):
    smer = prikaz[0].upper()
    if smer == 'S': return (r-1, s)
    if smer == 'V': return (r, s+1)
    if smer == 'J': return (r+1, s)
    if smer == 'Z': return (r, s-1)
    return None

def zoznam_dveri(mriezka, r, s):
    dvere = []
    if ma_dvere(mriezka[r][s], 'S'): dvere.append('SEVER')
    if ma_dvere(mriezka[r][s], 'V'): dvere.append('VYCHOD')
    if ma_dvere(mriezka[r][s], 'J'): dvere.append('JUH')
    if ma_dvere(mriezka[r][s], 'Z'): dvere.append('ZAPAD')
    return dvere

def je_platna_pozicia(r, s, riadky, stlpce):
    return 0 <= r < riadky and 0 <= s < stlpce

def zobrazi_miestnost(mriezka, r, s, stack=None, kroky=0, ma_kluc=False):
    print(f"=== MIESTNOSŤ {mriezka[r][s]} [{r},{s}] ===")
    print(f"Tvoje kroky: {kroky} | Klúč: {'Máš' if ma_kluc else 'Nemáš'}")

    dvere = zoznam_dveri(mriezka, r, s)
    print("Kam môžeš isť:", ", ".join(dvere) if dvere else "Žiadne")

    if stack and stack.top > 0:
        print(f"Cesta späť: {stack.see()}")


def main():
    mriezka = nacitaj_labyrint()
    ma_kluc = False
    start_r, start_s = najdi_start(mriezka)
    r, s = start_r, start_s
    stack = myStack(1000)
    kroky = 0
    start_pos = (start_r, start_s)
    start_time = time.time()

    riadky, stlpce = len(mriezka), len(mriezka[0])

    print("ESCAPE ROOM | SEVER/VYCHOD/JUH/ZAPAD/NAVRAT/KONIEC")

    while True:
        if ma_kluc and (r, s) == start_pos:
            elapsed = time.time() - start_time
            print(f"VÍŤAZSTVO! Našiel si KĽÚČ a úspešne si sa vrátil na štart!")
            print(f"Tvoje kroky: {kroky} | Čas: {elapsed:.1f}s")
            print("GRATULUJEM!")
            break

        zobrazi_miestnost(mriezka, r, s, stack, kroky, ma_kluc)

        prikaz = input("> ").strip().upper()
        print()
        if prikaz == "KONIEC": break

        if prikaz == "NAVRAT":
            if stack.top > 0:
                predosly_smer = stack.pop()
                if predosly_smer == "SEVER":
                    r += 1
                elif predosly_smer == "VYCHOD":
                    s -= 1
                elif predosly_smer == "JUH":
                    r -= 1
                elif predosly_smer == "ZAPAD":
                    s += 1
            else:
                print("Žiadny návrat!")
            kroky += 1
            continue

        nova_pozicia = posun_pozicia(r, s, prikaz)
        if nova_pozicia is None:
            print("Neplatný smer!")
            continue

        nova_r, nova_s = nova_pozicia

        if not ma_dvere(mriezka[r][s], prikaz[0]):
            print("V tomto smere nie sú dvere!")
            continue
        if not je_platna_pozicia(nova_r, nova_s, riadky, stlpce) or mriezka[nova_r][nova_s] == 0:
            print("Mimo labyrintu alebo stena!")
            continue

        stack.push(prikaz)
        r, s = nova_r, nova_s
        kroky += 1

        if mriezka[r][s] & 32 and not ma_kluc:
            ma_kluc = True
            print("Našiel si KĽÚČ! Teraz sa len vrátiť na štart...")

    print("Ďakujem za hru!")


if __name__ == "__main__":
    main()
