import math

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru Herona. Długości boków trójkąta wynoszą a, b, c."""
    
    polObw = (a + b + c) / 2
    Pole = math.sqrt(polObw * (polObw - a) * (polObw - b) * (polObw - c))
    return Pole

print("Podaj długości boków trójkąta:")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b <= c or a + c <= b or b + c <= a:
    raise ValueError("Podane boki nie spełniają warunku budowy trójkąta")

print("Pole podanego trójkąta wynosi:")
print(heron(a, b, c))