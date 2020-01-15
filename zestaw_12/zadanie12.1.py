import random

def wyszukiwanieLiniowe(k, ilosc):
    L = []
    for item in range (0, ilosc):
        L.append(int(random.uniform(0, k-1)))
    print(L)
    y = int(random.uniform(0, k-1))
    print("wyszukawana liczba: {}".format(y))
    listaY = []
    for item in range (0, ilosc):
        if L[item] == y:
            listaY.append(item)
    if len(listaY) == 0:
        print("ta liczba nie znajduje się w tablicy")
    else:
        print("szukana liczba znajduje się w tablicy w komórkach o indeksach:")
        print(listaY)

k = int(input("podaj zakres liczb naturalnych: "))
ilosc = int(input("podaj ilość liczb: "))
wyszukiwanieLiniowe(k, ilosc)