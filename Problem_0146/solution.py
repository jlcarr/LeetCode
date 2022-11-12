class LLNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

    def remove(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.reset_(key)
        #self.print()
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.reset_(key)
            node.val = value
        else:
            if self.tail:
                self.tail.next = LLNode(key, value, prev=self.tail)
                self.tail = self.tail.next
            else:
                self.head = LLNode(key, value)
                self.tail = self.head
            self.cache[key] = self.tail
        
        if len(self.cache) > self.capacity:
            del self.cache[self.head.key]
            new_head = self.head.next
            self.head.remove()
            self.head = new_head
            if self.head is None:
                self.tail = None

        #self.print()
    
    def reset_(self, key: int) -> None:
        node = self.cache[key]

        if node is self.tail:
            return node

        # remove
        if node is self.head:
            self.head = self.head.next
        #if node is self.tail:
        #    self.tail = node.prev
        node.remove()

        # append to end
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
        else:
            self.head = node
            self.tail = self.head

        return node

    def print(self):
        res = []
        for k in sorted(self.cache.keys()):
            res.append((k, self.cache[k].key, self.cache[k].val))
        print(res)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
