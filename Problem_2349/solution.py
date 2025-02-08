import heapq
class NumberContainers:

    def __init__(self):
        self.map = dict()
        self.invmap = dict()
        self.invalids = dict()

    def change(self, index: int, number: int) -> None:
        if index in self.map:
            prev = self.map[index]
            if prev not in self.invalids:
                self.invalids[prev] = set()
            self.invalids[prev].add(index)
        if number in self.invalids and index in self.invalids[number]:
            self.invalids[number].remove(index)
        self.map[index] = number
        if number not in self.invmap:
            self.invmap[number] = []
        heapq.heappush(self.invmap[number], index)
        

    def find(self, number: int) -> int:
        if number not in self.invmap or not self.invmap[number]:
            return -1
        if number in self.invalids:
            while self.invmap[number] and self.invmap[number][0] in self.invalids[number]:
                heapq.heappop(self.invmap[number])
        if not self.invmap[number]:
            return -1
        return self.invmap[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
