import unittest
import math
from points import Point


class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        if x1 == x2 == x3 or y1 == y2 == y3:
            raise ValueError("punkty są współliniowe")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):          # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[{}, {}, {}]".format(self.pt1, self.pt2, self.pt3)

    def __repr__(self):         # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle({}, {}, {}, {}, {}, {})".format(self.pt1.x, 
                        self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

    def __eq__(self, other):    # obsługa tr1 == tr2
        Lself = [self.pt1, self.pt2, self.pt3]
        Lother = [other.pt1, other.pt2, other.pt3]
        for punkt in Lself:
            if not punkt in Lother:
                return False
        return True

    def __ne__(self, other):    # obsługa tr1 != tr2
        return not self == other

    def center(self):           # zwraca środek trójkąta
        return Point((self.pt1.x + self.pt2.x + self.pt3.x)/3,
                     (self.pt1.y + self.pt2.y + self.pt3.y)/3)

    def area(self):             # pole powierzchni
        warBez = math.fabs((self.pt2.x - self.pt1.x) * (self.pt3.y - self.pt1.y) -
                           (self.pt2.y - self.pt1.y) * (self.pt3.x - self.pt1.x))
        return warBez/2

    def move(self, x, y):       # przesunięcie o (x, y)
        nowyPt1 = Point(self.pt1.x + x, self.pt1.y + y)
        nowyPt2 = Point(self.pt2.x + x, self.pt2.y + y)
        nowyPt3 = Point(self.pt3.x + x, self.pt3.y + y) 

        return Triangle(nowyPt1.x, nowyPt1.y, nowyPt2.x, nowyPt2.y, nowyPt3.x, nowyPt3.y)

    def make4(self):            # zwraca listę czterech mniejszych
        srodek1 = Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)
        srodek2 = Point((self.pt2.x + self.pt3.x)/2, (self.pt2.y + self.pt3.y)/2)
        srodek3 = Point((self.pt3.x + self.pt1.x)/2, (self.pt3.y + self.pt1.y)/2)
        Trojkat1 = Triangle(self.pt1.x, self.pt1.y, srodek1.x, srodek1.y, srodek3.x, srodek3.y)
        Trojkat2 = Triangle(srodek1.x, srodek1.y, srodek2.x, srodek2.y, srodek3.x, srodek3.y)
        Trojkat3 = Triangle(srodek1.x, srodek1.y, self.pt2.x, self.pt2.y, srodek2.x, srodek2.y)
        Trojkat4 = Triangle(srodek2.x, srodek2.y, self.pt3.x, self.pt3.y, srodek3.x, srodek3.y)
        L = [Trojkat1, Trojkat2, Trojkat3, Trojkat4]
        return L

# Kod testujący moduł.


class TestTriangle(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Triangle(1, 2, 3, 4, 5, 6)),
                         "[(1, 2), (3, 4), (5, 6)]")
        self.assertEqual(repr(Triangle(1, 2, 3, 4, 5, 6)),
                         "Triangle(1, 2, 3, 4, 5, 6)")

    def test_cmp(self):
        self.assertEqual(Triangle(2, 2, 6, 6, 8, 4), Triangle(8, 4, 6, 6, 2, 2))
        self.assertNotEqual(Triangle(2, 2, 6, 6, 8, 4), Triangle(1, 1, 6, 6, 10, 5))
    
    def test_center(self):
        self.assertEqual(Triangle.center(Triangle(2, 2, 6, 6, 8, 4)), Point(16/3, 4))
        self.assertEqual(Triangle.center(Triangle(-1, 1, 1, 4, 4, 1)), Point(4/3, 2))

    def test_area(self):
        self.assertEqual(Triangle.area(Triangle(2, 2, 6, 6, 8, 4)), 8)
        self.assertEqual(Triangle.area(Triangle(-1, 1, 1, 4, 4, 1)), 15/2)

    def test_move(self):
        self.assertEqual(Triangle.move(Triangle(2, 2, 6, 6, 8, 4), 3, 4), Triangle(5, 6, 9, 10, 11, 8))
        self.assertEqual(Triangle.move(Triangle(-1, 1, 1, 4, 4, 1), -2, 4), Triangle(-3, 5, -1, 8, 2, 5))

    def test_make4(self):
        self.assertEqual(Triangle.make4(Triangle(2, 2, 6, 6, 8, 4)), [Triangle(2, 2, 4, 4, 5, 3), Triangle(4, 4, 7, 5, 5, 3), Triangle(4, 4, 6, 6, 7, 5), Triangle(7, 5, 8, 4, 5, 3)])
        self.assertEqual(Triangle.make4(Triangle(-1, 1, 1, 4, 4, 1)), [Triangle(-1, 1, 0, 5/2, 3/2, 1), Triangle(0, 5/2, 5/2, 5/2, 3/2, 1), Triangle(0, 5/2, 1, 4, 5/2, 5/2), Triangle(5/2, 5/2, 4, 1, 3/2, 1)])

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
