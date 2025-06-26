from collections import deque
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        timeout = 0
        q = deque()
        result = []
        for i,v in enumerate(nums):
            q.append(i)
            while len(q) > k+1:
                q.popleft()
            if v == key:
                result += list(q)
                q.clear()
                timeout = k
            elif timeout > 0:
                result.append(i)
                timeout -= 1
                q.clear()
        return result

            
