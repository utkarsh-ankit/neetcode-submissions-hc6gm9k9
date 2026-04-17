class Node:
    def __init__(self, key=0, value=0):
        self.key=key
        self.value=value
        self.prev, self.next=None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hmap={}
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.delete(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.delete(self.hmap[key])
        node = Node(key, value)
        self.hmap[key] = node
        self.insert(node)
        if len(self.hmap) > self.capacity:
            lru = self.tail.prev
            self.delete(lru)
            del self.hmap[lru.key]