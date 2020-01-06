import random

class RandomQueue:

    def __init__(self, size = 10):
        self.items = size * [None]
        self.n = 0
        self.size = size

    def insert(self, item):
        if self.is_full():
            raise ValueError ("Kolejka pełna")
        self.items[self.n] = item
        self.n += 1

    def remove(self):   # zwraca losowy element
        if self.is_empty():
            raise ValueError ("Kolejka pusta")
        index = int(random.uniform(0, self.n-1))
        temp = self.items[index]
        self.items[index] = self.items[self.n-1]
        self.items[self.n-1] = None
        self.n -= 1
        return temp

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def clear(self):    # czyszczenie listy
        if self.is_empty():
            raise ValueError ("Kolejka pusta")
        while self.is_empty():
            self.items[self.n-1] = None
            self.n -= 1

import unittest

class TestRandomQueue(unittest.TestCase):

    def setUp(self):
        self.EmptyRQ = RandomQueue()
        self.FullRQ = RandomQueue()
        for item in range (0, 10):
            self.FullRQ.insert(item)

    def test_insert(self):
        with self.assertRaises(ValueError):
            self.FullRQ.insert(1)
        RQ = RandomQueue()
        for item in range (0, 5):
            RQ.insert(item)
        self.assertEqual(RQ.n, 5)
        self.assertEqual(RQ.items[4], 4)

    def test_remove(self):
        with self.assertRaises(ValueError):
            self.EmptyRQ.remove()
        RQ = RandomQueue()
        for item in range (0, 5):
            RQ.insert(item)
        print(RQ.remove())
        self.assertEqual(RQ.n, 4)

    def test_is_empty(self):
        self.assertTrue(RandomQueue.is_empty(self.EmptyRQ))
        self.assertFalse(RandomQueue.is_empty(self.FullRQ))

    def test_is_full(self):
        self.assertFalse(RandomQueue.is_full(self.EmptyRQ))
        self.assertTrue(RandomQueue.is_full(self.FullRQ))

    def test_clear(self):
        with self.assertRaises(ValueError):
            self.EmptyRQ.remove()
        RQ = RandomQueue()
        for item in range (0, 5):
            RQ.insert(item)
        RQ.clear()
        self.assertEqual(RQ.n, 0)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()