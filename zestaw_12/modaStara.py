def moda(k, ilosc):
    L = ListCreate(k, ilosc)
    iloscM = 1
    maxM = 0
    for item in range (0, len(L)-1):
        moda = L[item]
        if L[item] == L[item + 1]:
            iloscM += 1
            maxM = iloscM
        else:
            if maxM < iloscM:
                maxM = iloscM
                moda = L[item]
            iloscM = 1
    print(" moda to {}".format(moda))

def ListCreate(k, ilosc):
    L = []
    for item in range (0, ilosc):
        rand = int(random.uniform(0, k-1))
        L.append(rand)
    bubbleSort(L)
    return L

def bubbleSort(L):
    for itemFirst in range (0, len(L)):
        for itemSecond in range (0, len(L)-1):
            if L[itemSecond] > L[itemFirst]:
                L[itemFirst], L[itemSecond] = L[itemSecond], L[itemFirst]

k = int(input("podaj zakres liczb naturalnych: "))
ilosc = int(input("podaj ilość liczb: "))
print(moda(k, ilosc))
