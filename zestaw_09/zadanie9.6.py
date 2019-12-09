class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def count_leafs(top):
    if top is None:
        return 0
    left = count_leafs(top.left)
    right = count_leafs(top.right)
    if left == 0 and right == 0:
        return 1
    return left + right


def count_total(top):
    if top is None:
        return 0
    sum = top.data
    left = count_total(top.left)
    right = count_total(top.right)
    sum += left + right
    return sum


# BUDOWANIE DRZEWA
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(8)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(count_leafs(root))
print(count_total(root))
