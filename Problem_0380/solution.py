import random
class RandomizedSet:

    def __init__(self):
        self.table = [[]]
        self.load = 0
        self.balance = 0.5

    def insert(self, val: int) -> bool:
        hashval = hash(val)
        index = hashval % len(self.table)
        present = val in self.table[index]
        if present:
            return False
        self.table[index].append(val)
        self.load += 1
        return True

        if self.load / len(self.table) > self.balance:
            self._rehash()

    def remove(self, val: int) -> bool:
        hashval = hash(val)
        index = hashval % len(self.table)
        present = val in self.table[index]
        if not present:
            return False
        self.table[index].remove(val)
        self.load -= 1
        return True
        

    def getRandom(self) -> int:
        return random.choice(random.choice(self.table))

    def _rehash(self) -> None:
        newlen = int(self.load * self.balance * 2)
        newtable = []
        for i in range(newlen):
            newtable.append([])
        for bucket in self.table:
            for val in bucket:
                hashval = hash(val)
                index = hashval % newlen
                newtable[index].append(val)
        self.table = newtable

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
