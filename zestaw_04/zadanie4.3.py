def factorial(n):
    i = 1
    s = 1
    while i <= n:
        s = s * i
        i += 1
    return s

n = int(input("Podaj liczbę: "))
print (factorial(n))
