import unittest
from points import Point


class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Point(1, 2)), "(1, 2)")
        self.assertEqual(repr(Point(1, 2)), "Point(1, 2)")

    def test_cmp(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertTrue(Point(1, 2) != Point(3, 4))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))

    def test_sub(self):
        self.assertEqual(Point(1, 2) - Point(3, 4), Point(-2, -2))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(3, 4), 11)

    def test_cross(self):
        self.assertEqual(Point.cross(Point(1, 2), Point(3, 4)), -2)

    def test_length(self):
        self.assertEqual(Point.length(Point(3, 4)), 5)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
