class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full() == True:
            raise ValueError ("Kolejka jest pełna")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty() == True:
            raise ValueError ("Kolejka jest pusta")
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data

import unittest

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.EmptyQ = Queue()
        self.FullQ = Queue()
        for item in range (0, 5):
            self.FullQ.put(item)

    def test_is_empty(self):
        self.assertTrue(Queue.is_empty(self.EmptyQ))
        self.assertFalse(Queue.is_empty(self.FullQ))

    def test_is_full(self):
        self.assertFalse(Queue.is_full(self.EmptyQ))
        self.assertTrue(Queue.is_full(self.FullQ))

    def test_put(self):
        with self.assertRaises(ValueError):
            self.FullQ.put(1)
        Q = Queue()
        for item in range (0, 4):
            Q.put(item)
        self.assertEqual(Q.tail, 4)
        self.assertEqual(Q.items[3], 3)

    def test_get(self):
        with self.assertRaises(ValueError):
            self.EmptyQ.get()
        Q = Queue()
        for item in range (0, 4):
            Q.put(item)
        Q.get()
        self.assertEqual(Q.head, 1)
        self.assertEqual(Q.items[2], 2)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()