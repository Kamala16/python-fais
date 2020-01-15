import random

def moda_sort(L, left, right): 
    quicksort(L, 0, len(L)-1)
    if left+1 > right:
        return None
    mode = None
    modeNumber = 0
    temp = left
    tempNumber = 0
    while temp < right:
        temp += 1
        if L[temp] == L[temp-1]:
            tempNumber = tempNumber + 1
            if tempNumber > modeNumber:
                modeNumber = tempNumber
                mode = temp
        else:
            tempNumber = 1
    return mode

def ListCreate(k, ilosc):
    L = []
    for item in range (0, ilosc):
        rand = int(random.uniform(0, k-1))
        L.append(rand)
    return L

def quicksort(L, left, right):
    """Sortowanie szybkie wg Cormena str. 169."""
    if left >= right:
        return
    pivot = partition(L, left, right)
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)

def partition(L, left, right):
    """Zwraca indeks elementu rozdzielającego."""
    x = L[right]
    i = left
    for j in range(left, right):
        if L[j] <= x:
            swap(L, i, j)
            i += 1
    swap(L, i, right)
    return i

def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    L[left], L[right] = L[right], L[left]

k = int(input("podaj zakres liczb naturalnych: "))
ilosc = int(input("podaj ilość liczb: "))

Lista = ListCreate(k, ilosc)
print(Lista)
print(Lista[moda_sort(Lista, 0, len(Lista)-1)])