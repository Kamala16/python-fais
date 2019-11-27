import math

def solve1(a, b, c):
    # a * x + b * y + c = 0
    if a == 0 and b == 0 and c != 0:
        raise ValueError("Jeżeli a = 0 oraz b = 0 to c musi być równe 0")
    if a == b == c == 0:
        return "równanie tożsamościowe 0 = 0"
    elif a == 0 and b != 0:
        # 0x + by + c = 0
        y = - (c / b)
        return "rozwiązanie: prosta pozioma przechodząca przez punkt (0, {})".format(y)
    elif a != 0 and b == 0:
        # ax + 0y + c = 0
        x = - (c / a)
        return "rozwiązanie: prosta pionowa przechodząca przez puntk ({}, 0)".format(x)
    elif a != 0 and b != 0:
        # ax + by + c = 0
        x = - (c / a)
        y = - (c / b)
        kat = math.atan(- a / b)
        kat = math.degrees(kat)
        return "rozwiązanie: prosta przechodząca przez punkty: ({}, 0), (0, {}); Kąt nachylenia do osi OX: {}".format(x, y, kat)
        

print("Podaj współczynniki równania:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print(solve1(a, b, c))