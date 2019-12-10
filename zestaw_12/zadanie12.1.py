import random

def wyszukiwanieLiniowe():
    k = int(input("podaj zakres liczb naturalnych: "))
    ilosc = int(input("podaj ilość liczb: "))
    L = []
    for item in range (0, ilosc):
        rand = int(random.uniform(0, k-1))
        L.append(rand)
    print(L)
    y = int(random.uniform(0, k-1))
    print("wyszukawana liczba: {}".format(y))
    listaY = []
    for item in range (0, ilosc):
        if L[item] == y:
            listaY.append(item)
    return listaY
    
print(wyszukiwanieLiniowe())