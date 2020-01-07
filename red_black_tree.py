from queue import Queue
from stack import Stack

RED = 1
BLACK = 0


class Node:
    def __init__(self, value):
        self.value = value
        self.color = RED
        self.parent = None
        self.right = None
        self.left = None


class RedBlackTree:
    def __init__(self, initial=None):
        if initial:
            self.root = Node(initial)
            self.root.color = BLACK

    # https://github.com/Bibeknam/algorithmtutorprograms/blob/master/data-structures/red-black-trees/red_black_tree.py

    # def insert(self, value):
    #     if not self.root:
    #         self.root = Node(value)
    #     else:
    #         self._insert(self.root, value)

    # def _insert(self, node, value):
    #     if value > node.value:
    #         if not node.right:
    #             node.right = Node(value)
    #         else:
    #             self._insert(node.right, value)
    #     elif value < node.value:
    #         if not node.left:
    #             node.left = Node(value)
    #         else:
    #             self._insert(node.left, value)
    #     else:
    #         raise Exception(
    #             'Value %s is already presented in the tree' % value)

    # def is_empty(self):
    #     return not self.root
