# Escape Room LIFO (Stack)

## 1. Úvod
Tento dokument je súčasťou projektu **Escape Room – Labyrint**, ktorý bol vytvorený v programovacom jazyku Python.  
V projekte bola použitá dátová štruktúra **LIFO (Last In, First Out)**, implementovaná formou zásobníka (stack), ktorá slúži na ukladanie a spracovanie krokov hráča v labyrinte.

---

## 2. Dátová štruktúra LIFO (Last In, First Out)

### Popis
LIFO je dátová štruktúra, pri ktorej platí pravidlo, že **posledný vložený prvok je odstránený ako prvý**.  
Zásobník funguje podobne ako **kopa tanierov** – vždy sa berie ten, ktorý je navrchu.

### Ilustračný obrázok (schéma)
![LIFO-Operations-in-stack](https://github.com/user-attachments/assets/ae3daffa-678b-44da-bd58-d6effb966346)

---

## 3. Použitie LIFO v projekte

V projekte je LIFO implementované triedou `myStack`.  
Zásobník uchováva **históriu pohybov hráča**, aby bolo možné vrátiť sa späť pomocou príkazu `NAVRAT`.

### Princíp fungovania
- pri každom pohybe hráča sa smer uloží pomocou `push()`
  ```
      def push(self, smer):
        if self.top == self.capacity: raise OverflowError("Stack overflow")
        self.buffer[self.top] = smer
        self.top += 1

      # Volanie funkcie
      stack.push(prikaz)
  ```
- pri návrate sa posledný smer odstráni pomocou `pop()`, hráč sa presunie opačným smerom, než akým prišiel
 ```
     def pop(self):
        if self.top == 0: raise IndexError("Stack prázdny")
        self.top -= 1
        return self.buffer[self.top]

    # Volanie funkcie
    predosly_smer = stack.pop()
  ```

Týmto spôsobom je zabezpečený správny návrat v labyrinte.

---

## 4. Dôvody používania LIFO

Použitie dátovej štruktúry LIFO je v tomto projekte ideálne z nasledujúcich dôvodov:

- umožňuje presný návrat späť po poslednej ceste
- zjednodušuje implementáciu spätného pohybu
- efektívne spracúva posledné kroky hráča
- prirodzene rieši problém „undo“ operácií
- má jednoduchú a prehľadnú implementáciu

---

## 5. Ukážky z behu programu

### Zobrazenie aktuálnej miestnosti
<img width="288" height="111" alt="Screenshot 2026-01-22 at 19 22 25" src="https://github.com/user-attachments/assets/e787e7f2-4c49-4322-9b35-4f3697623bed" />


### Návrat pomocou zásobníka
<img width="333" height="249" alt="Screenshot 2026-01-22 at 19 22 45" src="https://github.com/user-attachments/assets/a1f78293-a60a-4e1a-8db0-6d571ba58ede" />


### Nájdenie kľúča
<img width="413" height="136" alt="Screenshot 2026-01-22 at 19 23 02" src="https://github.com/user-attachments/assets/61704d4d-8411-441c-8664-4fce5a3aecef" />


### Víťazstvo
<img width="500" height="103" alt="Screenshot 2026-01-22 at 19 23 13" src="https://github.com/user-attachments/assets/0ffc637e-a22b-4797-a160-141793731d4b" />

---

## 6. Osobný pohľad

Takže ja som mala na starosti projekt s využitím dátovej štruktúry LIFO - Labyrint. Priznám sa, keď som prvykrát otvorila zadanie a zbadala som príklad mapy labyrintu zostala som trošku prekvapená. Vôbec som nevedela, čo tie rôzne čísla znamenajú. Zabralo mi istý čas kým som pochopila, že hodnoty sa postupne pripočítavajú na základe toho, čo v danej izbe je, či sú to dvere, kľúč alebo štart. Túto dátovú štruktúru som už predtým poznala ale som rada, že som si vyskúšať implementovať ju do reálneho zábavého projektu. Mám pár nápadov, ako by som mohla projekt vylepšiť po vizuálnej stránke. Zatiaľ so nechala užívateľské prostredie riešené len pomocou výpisu textu do konzoly. Pohrávam sa s ideou ASCII artu, kde by mohla som každú miestnosť "nakresliť". Verím, že sa k tomuto projektu ešte vrátim a vylepším ho podľa môjho gusta. Celkovo ma tento projekt bavil :)
