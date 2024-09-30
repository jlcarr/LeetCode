class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.incs = []
        

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return
        self.stack.append(x)
        self.incs.append(0)
        #print('push', self.stack, self.incs)
        

    def pop(self) -> int:
        if not self.stack:
            return -1
        inc = self.incs.pop()
        if self.incs:
            self.incs[-1] += inc
        #print('pop', self.stack[-1] + inc, self.stack[:-1], self.incs)
        return self.stack.pop() + inc
        

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        k = min(k, len(self.stack))
        self.incs[k-1] += val
        #print('increment', self.stack, self.incs)
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
