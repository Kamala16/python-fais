Aleksandra Chrzanowska 31.01.2020

# Algorytm Prima

Algorytm służący do obliczania minimalnego drzewa rozpinającego dla podanego grafu.

- [Algorytm Prima](#algorytm-prima)
  - [Opis algorytmu](#opis-algorytmu)
  - [Złożoność](#z%c5%82o%c5%bcono%c5%9b%c4%87)
  - [Spis funkcji](#spis-funkcji)
      - [Algorytm Prima](#algorytm-prima-1)
      - [Wpisywanie do grafu](#wpisywanie-do-grafu)
      - [Wypisywanie stringa](#wypisywanie-stringa)
      - [Wczytaj z pliku](#wczytaj-z-pliku)
      - [Zapisz do Pliku](#zapisz-do-pliku)
      - [Generuj graf](#generuj-graf)
  - [Źródła](#%c5%b9r%c3%b3d%c5%82a)

## Opis algorytmu

Początkowo drzewo składa się z dowolnie wybranego wierzchołka (korzeń drzewa). W każdym kroku do drzewa jest dodawana krawędź o najmniejszej wadze, wychodząca z wierzchołków znajdujących się już w minimalnym drzewie rozpinającym wraz z wierzchołkiem do którego prowadzi.

Jest to algorytm zachłanny, ponieważ w każdym kroku do drzewa jest dodawana krawędź, która w danym momencie wnosi najmniejszą wagę do drzewa.

## Złożoność

Cały algorytm ma złożoność $\mathcal{O}(n^2)$.

Pętla while wykonuje się dla każdej nie spójnej części grafu, czyli pętla ma złożoność $\mathcal{O}(1)$.
```Python
    while len(wierzcholki) != len(wierzcholkiOdzwiedzone):
        # ...
```
Pierwsza pętla for ma złożoność $\mathcal{O}(n)$.
```Python
    for item in wierzcholkiOdzwiedzone:
        # ...
```
Razem te pętle dają złozoność $\mathcal{O}(n)$

Kolejna pętla for iteruje po wszystkich sąsiadach danego wierzchołka. W najgorszym przypadku wierzchołek może sąsiadować ze wszytkimi wierzchołkami (także z samym sobą) co daje nam złożoność $\mathcal{O}(n)$.
```Python
    for sasiad in listaSasiedztwa[item].items():
        # ...
```
Pierwsza instrukcja warunkowa if służy do przeszukiwania listy, które w pythonie ma średnia złożoność to $\mathcal{O}(1)$.
```Python
    if not sasiad[0] in wierzcholkiOdzwiedzone:
        # ...
```
Druga instrukcja warunkowa ma złożoność $\mathcal{O}(1)$.
```Python
    if temp < minWaga:
        # ...
```

## Spis funkcji

#### Algorytm Prima
Funkcja ta przyjmuje listę sąsiedztwa w postaci (dict+dict), wykonuje algorytm Prima i zwraca obliczone minimalne drzewo dla podanego grafu w postaci (dict+dict)
```Python
def algorytmPrima(listaSasiedztwa):
    """Funkcja z algorytmem Prima do znajdywania minimalnego drzewa dla grafu"""
    # ...
    return minDrzewo
```
#### Wpisywanie do grafu
Funkcja przyjmuje jako argumenty graf (postać (dict+dict)), wierzchołek, który chcemy wpisać do grafu oraz jego sąsiada i wagę krawędzi ich łączących. Następnie wpisuje odpowiednio do grafu podaną relację
```Python
def wpisywanieDoGrafu(graf, wierzcholek, sasiad, waga):
    """Funkcja do tworzenia grafu w postaci (dict+dict)"""
    # ...
```
#### Wypisywanie stringa
Funkcja po otrzymaniu grafu w postaci (dict+dict) zwraca listę sąsiedztwa jako string
```Python
def wypisywanieStr(lista):
    """Funkcja do wypisywania minimalnego drzewa jako listy sąsiedztwa"""
    # ...
    return drzewo
```
#### Wczytaj z pliku
Funkcja wczytuje z pliku listę sąsiedztwa grafu i zwraca reprezentacje (dict+dict) grafu.
```Python
def wczytajZPliku(nazwaPliku):
    """Funckja do wczytywania grafów z pliku w formie listy sasiedztwa"""
    # ...
    return listaSasiedztwa
```
#### Zapisz do Pliku
Funkcja przyjmuje graf w reprezentacji (dict+dict) i zapisuje go do pliku w formie listy sąsiedztwa.
```Python
def zapiszDoPliku(minDrzewo, nazwaPliku):
    """Funkcja do zapisywania minimalnego drzewa dla podanego grafu w formie listy sąsiedztwa"""
    # ...
```
#### Generuj graf
Funkcja przyjmuje jako argumenty liczbę wierzchołków oraz maksymalną wagę do generowania grafu podane wcześniej przez użytkownika. Następnie generuje losowy graf i zwraca go w postaci (dict+dict).
```Python
def generujGraf(liczbaWierzcholkow, maxWaga):
    """Funkcja do generowania losowego grafu"""
    # ...
    return graf
```

## Źródła
Wprowadzenie do algorytmów, Cormen Thomas H., Leiseron Charles E., Riverst Ronald L. Clifford Stein