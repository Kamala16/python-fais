x = input("Podaj dlugość miarki: ")
miarka = ""
for i in range(int(x)):
    miarka = "|...." + miarka

miarka = miarka + "|\n0"
for i in range(1, int(x)+1):
    miarka = miarka + ("%5d" %i) 
    
print (miarka)
