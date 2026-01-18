import time

class myStack:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Kapacita musí byť > 0")
        self.top = 0
        self.capacity = capacity
        self.buffer = [None] * capacity  # myType LIFO

    def push(self, data):  # void push(myType data)
        if self.top == self.capacity:
            raise OverflowError("Stack overflow")
        self.buffer[self.top] = data
        self.top += 1

    def pop(self):  # myType pop()
        if self.top == 0:
            raise IndexError("Stack prázdny")
        self.top -= 1
        data = self.buffer[self.top]
        self.buffer[self.top] = None
        return data

    def freeCap(self):  # int freeCap()
        return self.capacity - self.top

    def clear(self):  # void clear()
        self.top = 0

    def toString(self):  # String toString()
        return str(self.buffer[:self.top])

    def see(self):  # String see()
        return str(self.buffer[:self.top])

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
    smer = prikaz[0].upper()  # vezme prvý písmeno
    if smer == 'S': return (r-1, s)
    if smer == 'V': return (r, s+1)
    if smer == 'J': return (r+1, s)
    if smer == 'Z': return (r, s-1)
    return None  # Neplatný smer

def zoznam_dveri(mriezka, r, s):
    dvere = []
    if ma_dvere(mriezka[r][s], 'S'): dvere.append('SEVER')
    if ma_dvere(mriezka[r][s], 'V'): dvere.append('VYCHOD')
    if ma_dvere(mriezka[r][s], 'J'): dvere.append('JUH')
    if ma_dvere(mriezka[r][s], 'Z'): dvere.append('ZAPAD')
    return dvere

def je_platna_pozicia(r, s, riadky, stlpce):
    return 0 <= r < riadky and 0 <= s < stlpce

def zobrazi_miestnost(mriezka, r, s, stack=None, kroky=0):
    print(f"\n🎮 MIESTNOSŤ {mriezka[r][s]} [{r},{s}] | Kroky: {kroky}")
    dvere = zoznam_dveri(mriezka, r, s)
    print("DVERE:", ", ".join(dvere) if dvere else "Žiadne")
    if mriezka[r][s] & 32: print("🌟 KLÚČ NÁJDENÝ! 🌟")
    if stack and stack.top: print(f"🗺️ Cesta späť: {stack.see()}")

def main():
    mriezka = nacitaj_labyrint()
    r, s = najdi_start(mriezka)
    stack = myStack(100)
    kroky = 0
    start_pos = (r, s)
    start_time = time.time()

    print("🎮 ESCAPE ROOM LIFO | SEVER/VYCHOD/JUH/ZAPAD/NAVRAT/KONIEC")

    while True:
        zobrazi_miestnost(mriezka, r, s, stack, kroky)

        prikaz = input("> ").strip().upper()
        if prikaz == "KONIEC": break
        if prikaz == "NAVRAT":
            if stack.top:
                r, s = stack.pop()
                print("↩️ Návrat")
                kroky += 1
            else:
                print("❌ Žiadny návrat!")
            continue

        nova_pozicia = posun_pozicia(r, s, prikaz)
        if nova_pozicia is None:
            print("❌ Neplatný smer!")
            continue

        nova_r, nova_s = nova_pozicia

        stack.push((r, s))
        r, s = nova_r, nova_s
        kroky += 1

        # VÍŤAZSTVO
        if (mriezka[r][s] & 32) and (r, s) == start_pos:
            print(f"\n🏆 VÍŤAZTVO! {kroky} krokov, {time.time() - start_time:.1f}s")
            break

    print("Ďakujeme za hru! 👋")

if __name__ == "__main__":
    main()
