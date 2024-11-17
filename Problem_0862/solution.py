from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # min i+1-j | j<=i | cumsum[i+1] - cumsum[j] >= k
        # for each i: max j | cumsum[i+1] - k >= cumsum[j]
        # q in order, increasing, since we can tighten
        
        result = len(nums)+1
        q = deque([(0,-1)])
        acc = 0
        for i,v in enumerate(nums):
            acc += v
            while q and acc - q[0][0] >= k:
                result = min(result, i - q.popleft()[1])
            while q and q[-1][0] >= acc:
                q.pop()
            q.append((acc,i))
        if result == len(nums)+1:
            return -1
        return result
