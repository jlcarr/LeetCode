from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        monotonic_queue = deque()
        for i,n in enumerate(nums):
            # push to monotonic queue
            while len(monotonic_queue) > 0 and n > monotonic_queue[0][0]:
                monotonic_queue.popleft()
            monotonic_queue.appendleft((n,i))
            
            # after initial setup
            if i >= k-1:
                # check if need to pop queue
                if i >= monotonic_queue[-1][1] + k:
                    monotonic_queue.pop()

                # get solution
                result.append(monotonic_queue[-1][0])
            
        return result
