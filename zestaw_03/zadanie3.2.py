#Przykład 1:
#L = [3, 5, 4] ; L = L.sort()

#poprawny kod:
L = [3, 5, 4]
L.sort()
print (L)

#Przykład 2:
#x, y = 1, 2, 3

#za dużo argumentów dla przypisania do zmiennch

x, y = 1, 2 #poprawna wersja

#Przykład 3:
#X = 1, 2, 3; X[1] = 4

#Krotka to niezmienna lista, której wartość określamy podczas tworzenia i nie możemy jej zmieniać 

#Przykład 4:
#X = [1, 2, 3]; X[3] = 4

#przekraczamy rozmiar listy, aby dodać w tym przypadku coś w X[3] trzeba dodać nowy element listy

#użyź medoty append lub insert

#Przykład 5:
#X = "abc"; X.append("d")

#w tym przypadku x jest referencją do stringa "abc" i nie można go zmieniać

#Przykład 6:
#map(pow, range(8))

#brakuje potęgi dla funkcji pow
