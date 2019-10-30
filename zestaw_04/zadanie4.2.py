def miarka():
    x = input("Podaj długość miarki: ")
    miarka = ""
    
    for i in range(int(x)):
        miarka = "|...." + miarka

    miarka = miarka + "|\n0"
    
    for i in range(1, int(x)+1):
        miarka = miarka + ("%5d" %i)

    return miarka

def prostokat():
   
    x = input("podaj ilość kratek na szerokość: ")
    y = input("podaj ilość kratek na wysokość: ")
 
    prostokat = ""
 
    for i in range(int(y)):
        for j in range(int(x)):
            prostokat = prostokat + "+---"
        prostokat = prostokat + "+\n" + ((j+1) * "|   ") + "|\n"
    prostokat = prostokat + (int(x) * "+---") + "+"
    
    return prostokat


print (miarka())
print ("\n\n\n")
print (prostokat())
