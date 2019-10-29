x = input("podaj ilość kratek na szerokość: ")
y = input("podaj ilość kratek na wysokość: ")

prostokat = ""

for i in range(int(y)):
    for j in range(int(x)):
        prostokat = prostokat + "+---"
    prostokat = prostokat + "+\n" + ((j+1) * "|   ") + "|\n"
prostokat = prostokat + (int(x) * "+---") + "+"
print (prostokat)
