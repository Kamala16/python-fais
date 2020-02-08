"""Algorytm Prima

Aleksandra Chrzanowska"""

import random

def algorytmPrima(listaSasiedztwa):
    """Funkcja z algorytmem Prima do znajdywania minimalnego drzewa dla grafu"""
    wierzcholki = []
    wierzcholkiOdzwiedzone = []
    minDrzewo = {}
    
    for item in listaSasiedztwa:
        wierzcholki.append(item)
    
    wierzcholkiOdzwiedzone.append(wierzcholki[0])

    while len(wierzcholki) != len(wierzcholkiOdzwiedzone):
        minWaga = float("inf")
        for item in wierzcholkiOdzwiedzone:
            for sasiad in listaSasiedztwa[item].items():
                if not sasiad[0] in wierzcholkiOdzwiedzone:
                    temp = sasiad[1]
                    if temp < minWaga:
                        minWaga = temp
                        minSasiad = sasiad[0]
                        rodzic = item
        wpisywanieDoGrafu(minDrzewo, rodzic, minSasiad, minWaga)
        wierzcholkiOdzwiedzone.append(minSasiad)
    return minDrzewo

def wpisywanieDoGrafu(graf, wierzcholek, sasiad, waga):
    """Funkcja do tworzenia grafu w postaci (dict+dict)"""
    if wierzcholek in graf:
        graf[wierzcholek][sasiad] = waga
    else:
        graf[wierzcholek] = {sasiad: waga}

def wypisywanieStr(lista):
    """Funkcja do wypisywania minimalnego drzewa jako listy sasiedztwa"""
    drzewo = ""
    for rodzic in lista:
        wierzcholek = str(rodzic) + ": "
        for sasiad in lista[rodzic]:
            wierzcholek = wierzcholek + str(sasiad) + "(" + str(lista[rodzic][sasiad]) + ") "
        drzewo = drzewo + "\n" + wierzcholek
    return drzewo

def wczytajZPliku(nazwaPliku):
    """Funckja do wczytywania grafów z pliku w formie listy sasiedztwa"""
    listaSasiedztwa = {}
    plik = open(nazwaPliku, 'r')
    for line in plik:
        wierzcholek, sasiedzi = line.split(":")
        sasiedzi = sasiedzi.strip()
        listaSasiadow = sasiedzi.split(' ')
        for item in listaSasiadow:
            sasiad = item.split('(')
            waga = sasiad[1].split(')')
            wpisywanieDoGrafu(listaSasiedztwa, int(wierzcholek), int(sasiad[0]), int(waga[0]))
    plik.close()
    return listaSasiedztwa

def zapiszDoPliku(minDrzewo, nazwaPliku):
    """Funkcja do zapisywania minimalnego drzewa dla podanego grafu w formie listy sąsiedztwa"""
    plik = open(nazwaPliku, 'w')
    plik.write("Lista sasiedztwa minimalnego drzewa dla podanego grafu:\n")
    plik.write(wypisywanieStr(minDrzewo))
    plik.close()

def generujGraf(liczbaWierzcholkow, maxWaga):
    """Funkcja do generowania losowego grafu"""
    graf = {}
    for licznik in range(liczbaWierzcholkow):
        liczbaSasiadow = random.randint(0, liczbaWierzcholkow)
        if liczbaSasiadow == 0 and licznik not in graf:
            graf[licznik] = {}
        while liczbaSasiadow > 0:
            sasiad = random.randint(0, liczbaWierzcholkow)
            waga = random.randint(1, maxWaga)
            wpisywanieDoGrafu(graf, sasiad, licznik, waga)
            wpisywanieDoGrafu(graf, licznik, sasiad, waga)
            liczbaSasiadow -= 1
    
    print("Wygenerowano poniższy graf:")
    print(wypisywanieStr(graf))
    return graf

def main():
    x = int(input("Wybierz opcję:\n1. Wczytaj graf z pliku.\n2. Wygeneruj losowy graf.\n3. Zakoncz program.\n"))
    while x != 3:
        if x == 1:
            nazwaPlikuWczytaj = input("Podaj nazwę pliku do wczytania:\n")
            lista = wczytajZPliku(nazwaPlikuWczytaj)
            minDrzewo = algorytmPrima(lista)
            nazwaPlikuZapisz = input("Podaj nazwę pliku do zapisania:\n")
            zapiszDoPliku(minDrzewo, nazwaPlikuZapisz)
            print("Minimalne drzewo zostało zapisane do pliku")
        elif x == 2:
            liczbaWierzcholkow = int(input("Podaj liczbę wierzchołków dla grafu: "))
            maxWaga = int(input("Podaj maksymalna wartość krawędzi: "))
            algorytmPrima(generujGraf(liczbaWierzcholkow, maxWaga))
            nazwaPlikuZapisz = input("Podaj nazwę pliku do zapisania:\n")
            zapiszDoPliku(minDrzewo, nazwaPlikuZapisz)
            print("Minimalne drzewo zostało zapisane do pliku")
        else:
            print("Nie wybrałeś żadnej z dostępnych opcji.\n")
        x = int(input("Wybierz opcję:\n1. Wczytaj graf z pliku.\n2. Wygeneruj losowy graf.\n3. Zakoncz program.\n"))
    return 0

if __name__ == "__main__":
    main()