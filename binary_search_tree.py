from queue import Queue
from stack import Stack


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self, initial=None):
        self.root = Node(initial) if initial else None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value > node.value:
            if not node.right:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
        elif value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            raise Exception(
                'Value %s is already presented in the tree' % value)

    def is_empty(self):
        return not self.root

    def size(self, use='recursion'):
        if use == 'recursion':
            return self.size_recursion()
        elif use == 'stack':
            return self.size_stack()
        raise Exception('Can not calculate size using %s' % use)

    def size_recursion(self, node=-1):
        if node == -1:
            node = self.root
        if not node:
            return 0
        return 1 + self.size_recursion(node.left) + self.size_recursion(node.right)

    def size_stack(self):
        size = 0

        stack = Stack()
        if self.root:
            stack.push(self.root)

        while not stack.is_empty():
            current = stack.pop()
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)
            size += 1

        return size

    def height(self, node=-1):
        if node == -1:
            node = self.root
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def inorder(self):
        arr = []
        self._inorder(self.root, arr)
        return arr

    def _inorder(self, node, arr):
        if node:
            self._inorder(node.left, arr)
            arr.append(node.value)
            self._inorder(node.right, arr)

    def preorder(self):
        arr = []
        self._preorder(self.root, arr)
        return arr

    def _preorder(self, node, arr):
        if node:
            arr.append(node.value)
            self._preorder(node.left, arr)
            self._preorder(node.right, arr)

    def postorder(self):
        arr = []
        self._postorder(self.root, arr)
        return arr

    def _postorder(self, node, arr):
        if node:
            self._postorder(node.left, arr)
            self._postorder(node.right, arr)
            arr.append(node.value)

    def levelorder(self):
        arr = []

        queue = Queue()
        if self.root:
            queue.enqueue(self.root)

        while not queue.is_empty():
            current = queue.dequeue()
            arr.append(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)

        return arr

    def validate_bst(self, node=-1, mini=None, maxi=None):
        # validate tree for bst property
        if node == -1:
            node = self.root
        if not node:
            return True
        if mini is not None and node.value < mini:
            return False
        if maxi is not None and node.value > maxi:
            return False
        return (
            self.validate_bst(node=node.left, mini=mini, maxi=node.value-1) and
            self.validate_bst(node=node.right, mini=node.value+1, maxi=maxi)
        )


tree = BinarySearchTree(initial=4)
tree.root.left = Node(2)
tree.root.right = Node(5)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.insert(6)
tree.insert(7)
tree.insert(-1)
tree.insert(-3)
tree.insert(12)
tree.insert(14)

if (tree.validate_bst()):
    print("Valid binary search tree")
else:
    print("Invalid binary search tree")

print(tree.inorder())
print(tree.preorder())
print(tree.postorder())
print(tree.levelorder())
print(tree.size())
print(tree.size(use='stack'))
print(tree.height())
