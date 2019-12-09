class Node:
    """Klasa reprezentująca węzeł listy dwukierunkowej."""

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        # self.prev = prev

    def __str__(self):
        return str(self.data)


class SortedList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __str__(self):
        if self.length == 0:
            return '[]'
        s = "[ "
        node = self.head
        while node != self.tail:
            s = s + str(node) + ", "
            node = node.next
        s = s + str(self.tail) + "]"
        return s

    def is_empty(self):
        return self.length == 0

    def insert(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:
            if self.head.data > node.data:
                node.next = self.head
                self.head = node
            elif self.tail.data < node.data:
                self.tail.next = node
                self.tail = node
            else:
                tempNode = self.head
                while tempNode.next.data < node.data:
                    tempNode = tempNode.next
                node.next = tempNode.next
                tempNode.next = node
        self.length += 1

    def remove(self):       # zwraca element największy (node)
        if self.length == 0:
            raise ValueError("lista jest pusta")
        elif self.head is self.tail:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            tempNode = self.head
            while tempNode.next != self.tail:
                tempNode = tempNode.next
            self.tail = tempNode
            return node

    def merge(self, other):  # scalanie dwóch list posortowanych
        if other.length == 0:
            return self
        if self.length == 0:
            self.head == other.head
        tempNode = other.head
        while tempNode.next != other.tail:
            print(tempNode)
            self.insert(Node(tempNode.data))
            tempNode = tempNode.next
        self.insert(tempNode)
        self.insert(other.tail)
        return self

    def clear(self):        # czyszczenie listy
        self.head = None
        self.tail = None
        self.length = 0


L = SortedList()
M = SortedList()
print(L.is_empty())
print(str(L))
L.insert(Node(5))
L.insert(Node(2))
L.insert(Node(4))
L.insert(Node(9))
print(L)
L.remove()
M.insert(Node(1))
M.insert(Node(3))
M.insert(Node(8))
print(str(L))
print(M)
M.merge(L)
print(str(L))
print(M)
L.clear()
print(str(L))
