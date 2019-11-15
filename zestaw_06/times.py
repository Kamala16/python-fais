class Time:
    """Klasa reprezentująca odcinek czasu."""

    def __init__(self, s=0):
        """Zwraca instancję klasy Time."""
        self.s = int(s)

    def __str__(self):
        """Zwraca string 'hh:mm:ss'."""
        h = self.s // 3600
        sec = self.s - h * 3600
        m = sec // 60
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        """Zwraca string 'Time(s)'."""
        return "Time({0})".format(self.s)

    def __add__(self, other):
        """Dodawanie odcinków czasu."""
        return Time(self.s + other.s)

    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return self.s != other.s

    def __lt__(self, other):
        return self.s < other.s

    def __le__(self, other):
        return self.s <= other.s

    # nadmiarowe
    #def __gt__(self, other):
    #    return self.s > other.s

    # nadmiarowe
    #def __ge__(self, other):
    #    return self.s >= other.s

    def __int__(self):                  # int(time1)
        """Konwersja odcinka czasu do int."""
        return self.s

# Kod testujący moduł.

import unittest

class TestTime(unittest.TestCase):

    def setUp(self): 
        self.jeden = Time(3600)
        self.dwa = Time(3601)
        self.trzy = Time(3665)
        self.cztery = Time(18540)

    def test_print(self):       # test str() i repr()
        self.assertEqual(str(self.jeden), '01:00:00')
        self.assertEqual(str(self.dwa), '01:00:01')
        self.assertEqual(str(self.trzy), '01:01:05')
        self.assertEqual(str(self.cztery), '05:09:00')
        self.assertEqual(repr(self.jeden), 'Time(3600)')
        self.assertEqual(repr(self.dwa), 'Time(3601)')
        self.assertEqual(repr(self.trzy), 'Time(3665)')
        self.assertEqual(repr(self.cztery), 'Time(18540)')
        

    def test_add(self):
        #self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(self.jeden + self.dwa, Time(7201))


    def test_cmp(self):
        # Można sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(self.jeden == Time(3600))
        self.assertTrue(self.dwa != self.trzy)
        self.assertTrue(self.cztery > self.trzy)

    def test_int(self):
        self.assertEqual(int(Time(55)), 55)

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy