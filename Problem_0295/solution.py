import heapq

class MedianFinder:

    def __init__(self):
        self.lower = []
        self.greater = []

    def addNum(self, num: int) -> None:
        if not self.greater or num > self.greater[0]:
            heapq.heappush(self.greater, num)
        else:
            heapq.heappush(self.lower, -num)
        
        # reorder
        while self.greater and self.lower and self.greater[0] < -self.lower[0]:
            l,g = -heapq.heappop(self.lower), heapq.heappop(self.greater)
            heapq.heappush(self.greater, l)
            heapq.heappush(self.lower, -g)
        
        # rebalance
        while len(self.lower) > len(self.greater):
            heapq.heappush(self.greater, -heapq.heappop(self.lower))
        while len(self.greater) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.greater))
            
        #print((self.lower, self.greater)) 

    def findMedian(self) -> float:
        if len(self.lower) == len(self.greater):
            return (self.greater[0] - self.lower[0])/2
        elif len(self.lower) > len(self.greater):
            return -self.lower[0]
        else:
            return self.greater[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
