class FreqStack:

    def __init__(self):
        self.val_to_freq = dict()
        self.freq_to_stack = dict()
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val not in self.val_to_freq:
            self.val_to_freq[val] = 0
        self.val_to_freq[val] += 1
        f = self.val_to_freq[val]
        if f not in self.freq_to_stack:
            self.freq_to_stack[f] = []
        self.freq_to_stack[f].append(val)

        self.max_freq = max(self.max_freq, f)

    def pop(self) -> int:
        res = self.freq_to_stack[self.max_freq].pop()
        self.val_to_freq[res] -= 1
        if not self.freq_to_stack[self.max_freq]:
            del self.freq_to_stack[self.max_freq]
            self.max_freq -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
