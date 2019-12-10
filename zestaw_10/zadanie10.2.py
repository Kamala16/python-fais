class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full() == True:
            raise ValueError("Stos jest pełny")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty() == True:
            raise ValueError("Stos jest pusty")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data

import unittest

class TestStack(unittest.TestCase):

    def setUp(self):
        self.S = Stack()
        self.F = Stack()
        for item in range (self.F.size):
            self.F.push(item)

    def test_is_empty(self):
        self.assertTrue(Stack.is_empty(self.S))
        self.assertFalse(Stack.is_empty(self.F))

    def test_is_full(self): 
        self.assertFalse(Stack.is_full(self.S))
        self.assertTrue(Stack.is_full(self.F))

    def test_push(self):
        with self.assertRaises(ValueError):
            self.F.push(3)
        T = Stack()
        for item in range (0, 4):
            T.push(item)
        self.assertEqual(T.n, 4)
        self.assertEqual(T.items[3], 3)

    def test_pop(self):
        with self.assertRaises(ValueError):
            self.S.pop()
        T = Stack()
        for item in range (0, 4):
            T.push(item)
        T.pop()
        self.assertEqual(T.n, 3)
        self.assertEqual(T.items[2], 2)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()


