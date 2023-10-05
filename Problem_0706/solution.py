class MyHashMap:

    def __init__(self):
        self.table = [[]]
        self.load = 0

    def put(self, key: int, value: int) -> None:
        self.remove(key)

        l = len(self.table)
        # rehash
        if ((self.load + 1) / l) > 0.75:
            new_table = [[] for _ in range(l*2)]
            for bucket in self.table:
                for k,v in bucket:
                    index = self._hash(k) % len(new_table)
                    new_table[index].append((k,v))
            self.table = new_table
        # search
        index = self._hash(key) % len(self.table)
        self.table[index].append((key, value))
        self.load += 1

    def get(self, key: int) -> int:
        index = self._hash(key) % len(self.table)
        for k,v in self.table[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        if self.get(key) == -1:
            return
        index = self._hash(key) % len(self.table)
        self.table[index] = [
            (k,v) 
            for k,v in self.table[index]
            if k != key
            ]
        self.load -= 1

    def _hash(self, v):
        return (v << 16) ^ (v >> 16) ^ (0xA1B3C5D7)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
