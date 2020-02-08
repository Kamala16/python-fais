#I SPOSÓB TWORZENIA SŁOWNIKA
D = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000}

"""II SPOSÓB TWORZENIA SŁOWNIKA
D = {}
D["I"] = 1
D["V"] = 5
D["X"] = 10
D["L"] = 50
D["C"] = 100
D["D"] = 500
D["M"] = 1000"""

x = input("symbol rzymski: ")
print (D[x])
