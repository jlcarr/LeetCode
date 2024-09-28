class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.q = [None] * k
        self.start = 0
        self.size = 0
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.start = (self.start - 1) % self.k
        self.q[self.start] = value
        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[(self.start + self.size) % self.k] = value
        self.size += 1
        return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start + 1) % self.k
        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.start]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.start + self.size - 1) % self.k]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
