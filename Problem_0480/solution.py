import heapq
from collections import Counter
class Solution:
    def clean_heap(self, heap, remove, neg=1):
        while heap and neg*heap[0] in remove and remove[neg*heap[0]] > 0:
            remove[neg*heap[0]] -= 1
            heapq.heappop(heap)
            
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lower_heap, lower_remove = [], Counter()
        upper_heap, upper_remove = [], Counter()
        
        #init
        for i in range(k):
            heapq.heappush(lower_heap, -nums[i])
        for i in range(k//2):
            heapq.heappush(upper_heap, -heapq.heappop(lower_heap))
        
        result = []
        if k%2 == 1:
            result.append(-lower_heap[0])
        else:
            result.append((upper_heap[0]-lower_heap[0])/2)
        
        for i in range(k,len(nums)):
            #print(lower_heap, lower_remove)
            #print(upper_heap, upper_remove)
            #print()
            # remove old
            drop = nums[i-k]
            if -lower_heap[0] >= drop:
                lower_remove[drop] += 1
            else:
                upper_remove[drop] += 1
            # insert new
            if upper_heap and upper_heap[0] < nums[i]:
                heapq.heappush(upper_heap, nums[i])
            else:
                heapq.heappush(lower_heap, -nums[i])
            self.clean_heap(lower_heap, lower_remove, neg=-1)
            self.clean_heap(upper_heap, upper_remove)
            
            # rebalance
            while len(lower_heap) - lower_remove.total() - (k%2) > len(upper_heap) - upper_remove.total():
                heapq.heappush(upper_heap, -heapq.heappop(lower_heap))
                self.clean_heap(lower_heap, lower_remove, neg=-1)
            while len(lower_heap) - lower_remove.total() - (k%2) < len(upper_heap) - upper_remove.total():
                heapq.heappush(lower_heap, -heapq.heappop(upper_heap))
                self.clean_heap(upper_heap, upper_remove)
            #print(len(lower_heap) - lower_remove.total() - (k%2), len(upper_heap) - upper_remove.total())
            # compute median
            if k%2 == 1:
                result.append(-lower_heap[0])
            else:
                result.append((upper_heap[0]-lower_heap[0])/2)
                
        return result
