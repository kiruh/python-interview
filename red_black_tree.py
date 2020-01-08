import sys

BLACK = 0
RED = 1


class Node:
    def __init__(self, data):
        self.data = data
        self.color = RED
        self.parent = None
        self.right = None
        self.left = None


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = BLACK
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    # rotate left at node x
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # insert the key to the tree in its appropriate position
    # and fix the tree
    def insert(self, data):
        # Ordinary Binary Search Insertion
        node = Node(data)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = RED

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        # if new node is a root node, simply return
        if node.parent == None:
            node.color = BLACK
            return

        # if the grandparent is None, simply return
        if node.parent.parent == None:
            return

        # Fix the tree
        self.__fix_insert(node)

    # fix the red-black tree
    def __fix_insert(self, node):
        while node.parent.color == RED:
            # check if parent is right child
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    # case 3.1
                    uncle.color = BLACK
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # case 3.2.2 (triangle)
                        node = node.parent
                        self.right_rotate(node)
                    # case 3.2.1 (line)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    # mirror case 3.1
                    uncle.color = BLACK
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # mirror case 3.2.2 (triangle)
                        node = node.parent
                        self.left_rotate(node)
                    # mirror case 3.2.1(line)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = BLACK

    def __print_helper(self, node, indent, last):
        # print the tree structure on the screen
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.data) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    # print the tree structure on the screen
    def pretty_print(self):
        self.__print_helper(self.root, "", True)


tree = RedBlackTree()
tree.insert(1)
tree.insert(2)
tree.insert(6)
tree.insert(4)
tree.insert(5)
tree.pretty_print()
