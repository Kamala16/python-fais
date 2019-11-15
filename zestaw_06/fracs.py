import unittest
from math import gcd


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if(self.y == 1):
            return "{}".format(self.x)
        else:
            return "{}/{}".format(self.x, self.y)

    def __repr__(self):         # zwraca "Frac(x, y)"
        return "Frac({}, {})".format(self.x, self.y)

    def __add__(self, other):  # frac1 + frac2
        nww = self.y * other.y // gcd(self.y, other.y)
        licznik1 = self.x * (nww // self.y)
        licznik2 = other.x * (nww // other.y)
        return Frac(licznik1 + licznik2, nww)

    def __sub__(self, other):   # frac1 - frac2
        nww = self.y * other.y // gcd(self.y, other.y)
        licznik1 = self.x * (nww // self.y)
        licznik2 = other.x * (nww // other.y)
        return Frac(licznik1 - licznik2, nww)

    def __mul__(self, other):  # frac1 * frac2
        return Frac(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):   # frac1 / frac2
        return Frac(self.x * other.y, self.y * other.x)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        nww = self.y * other.y // gcd(self.y, other.y)
        licznik1 = self.x * (nww // self.y)
        licznik2 = other.x * (nww // other.y)
        return licznik1 == licznik2

    def __ne__(self, other):
        nww = self.y * other.y // gcd(self.y, other.y)
        licznik1 = self.x * (nww // self.y)
        licznik2 = other.x * (nww // other.y)
        return licznik1 != licznik2

    def __lt__(self, other):
        nww = self.y * other.y // gcd(self.y, other.y)
        licznik1 = self.x * (nww // self.y)
        licznik2 = other.x * (nww // other.y)
        return licznik1 < licznik2

    def __le__(self, other):
        nww = self.y * other.y // gcd(self.y, other.y)
        licznik1 = self.x * (nww // self.y)
        licznik2 = other.x * (nww // other.y)
        return licznik1 <= licznik2

    def __float__(self):        # float(frac)
        return float(self.x / self.y)

# Kod testujący moduł.


class TestFrac(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Frac(3, 4)), "3/4")
        self.assertEqual(str(Frac(6, 1)), "6")
        self.assertEqual(repr(Frac(3, 4)), "Frac(3, 4)")

    def test_add(self):
        self.assertEqual(Frac(3, 4) + Frac(5, 6), Frac(19, 12))
        self.assertEqual(Frac(3, 4) + Frac(-5, 6), Frac(-1, 12))

    def test_sub(self):
        self.assertEqual(Frac(3, 4) - Frac(5, 6), Frac(-1, 12))
        self.assertEqual(Frac(3, 4) - Frac(-5, 6), Frac(19, 12))

    def test_mul(self):
        self.assertEqual(Frac(3, 4) * Frac(5, 6), Frac(15, 24))
        self.assertEqual(Frac(3, 4) * Frac(-5, 6), Frac(-15, 24))

    def test_div(self):
        self.assertEqual(Frac(3, 4) / Frac(5, 6), Frac(18, 20))
        self.assertEqual(Frac(3, 4) / Frac(-5, 6), Frac(18, -20))

    def test_pos(self):
        self.assertEqual(+Frac(3, 4), Frac(3, 4))

    def test_neg(self):
        self.assertEqual(-Frac(3, 4), Frac(-3, 4))

    def test_invert(self):
        self.assertTrue(~Frac(3, 4), Frac(4, 3))

    def test_cmp(self):
        self.assertTrue(Frac(1, 2) == Frac(2, 4))
        self.assertTrue(Frac(3, 4) != Frac(5, 6))
        self.assertTrue(Frac(3, 4) < Frac(5, 6))

    def test_float(self):
        self.assertEqual(float(Frac(3, 4)), 0.75)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
