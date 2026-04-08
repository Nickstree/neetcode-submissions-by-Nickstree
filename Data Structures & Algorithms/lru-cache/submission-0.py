class Node:
    def __init__(self, key:int = 0, val: int = 0) -> None:
        self.key, self.val = key, val
        self.next, prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.cap = capacity
        self.dummy_head, self.dummy_tail = Node(), Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def remove(self, key: int):
        node = self.data[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        self.data.pop(key)

    def insert(self, key: int, val: int):
        node = self.data[key] = Node(key, val)
        left, right = self.dummy_head, self.dummy_head.next
        left.next = right.prev = node
        node.prev, node.next = left, right

    def get(self, key: int) -> int:
        node = self.data.get(key)
        if node:
            val = node.val
            self.remove(key)
            self.insert(key, val)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.data.get(key)
        if node:
            self.remove(key)
            self.insert(key, value)
        else:
            self.insert(key, value)
            while len(self.data) > self.cap:
                self.remove(self.dummy_tail.prev.key)


