class MyHashSet:

    def __init__(self):
        self.table = [[]]
        self.content = 0
        self.max_load = 0.75
        
    def _hash(self, key: int) -> None:
        return key % len(self.table)

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        if  (self.content + 1) / len(self.table) > self.max_load:
            old_table = self.table
            self.table = [[] for i in range(2*len(old_table))]
            for bucket in old_table:
                for k in bucket:
                    self.table[self._hash(k)].append(k)

        self.table[self._hash(key)].append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        self.table[self._hash(key)].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.table[self._hash(key)]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
