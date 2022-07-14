import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        not_removed = dict()
        
        # init
        for i in range(k):
            heapq.heappush(heap, -nums[i])
            
        result = [-heap[0]]
            
        i = 0
        while i + k < len(nums):
            # leave
            leaving = nums[i]
            if -heap[0] == leaving:
                heapq.heappop(heap)
            else:
                if leaving not in not_removed:
                    not_removed[leaving] = 0
                not_removed[leaving] += 1
            
            # enter
            entering = nums[i+k]
            heapq.heappush(heap, -entering)
            
            # clean heap
            while -heap[0] in not_removed:
                clean = -heapq.heappop(heap)
                not_removed[clean] -= 1
                if not_removed[clean] == 0:
                    del not_removed[clean]
            
            # update solution
            result.append(-heap[0])
            
            # continue
            i += 1
        
        return result
                
