sekwencja = ([],[4],(1,2),[3,4],(5,6,7))

sumaLiczb = []

liczebnosc = len(sekwencja)

for i in range(liczebnosc):
    rozmiar = len(sekwencja[i])
    temp = 0
    for j in range(rozmiar):
        temp = temp + sekwencja[i][j]
    
    sumaLiczb.append(temp)
print (sumaLiczb)
