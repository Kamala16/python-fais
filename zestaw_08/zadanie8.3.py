import random
import math

def calc_pi(n):
    """Obliczanie liczby pi metodą Monte Carlo. n oznacza liczbę losowanych punktów."""
    
    k, i = 0, 1

    while i <= n:

        x = random.random()
        y = random.random()

        if math.pow(x, 2) + math.pow(y, 2) <= 1:
            k += 1
        i += 1
    p = 4 * k / n
    return p

print(calc_pi(100))

""" n = 100 -> pi = 3,12;
    n = 1000 -> pi = 3,16;
    n = 10000 -> pi = 3,1444
    n = 100000 -> pi = 3,144
    n = 1000000 -> pi = 3,141404
    n = 10000000 -> pi = 3,1412728"""