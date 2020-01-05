class SListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        self.head = SListNode(data=data, next=self.head)

    def append(self, data):
        if not self.head:
            self.head = SListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = SListNode(data=data)

    def remove(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None


class DListNode:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_head = DListNode(data=data, next=self.head)
        if self.head:
            self.head.prev = new_head
        self.head = new_head

    def append(self, data):
        if not self.head:
            self.head = DListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = DListNode(data=data, prev=curr)

    def remove(self, key):
        elem = self.find(key)
        if not elem:
            return
        if elem.prev:
            elem.prev.next = elem.next
        if elem.next:
            elem.next.prev = elem.prev
        if elem is self.head:
            self.head = elem.next
        elem.prev = None
        elem.next = None
