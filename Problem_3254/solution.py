from collections import deque
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        results = []
        q = deque()
        prev = nums[0]-1
        for i,v in enumerate(nums):
            if q and q[-1] == i:
                q.pop()
            if v != prev+1 and k > 1:
                q.appendleft(i+k-1)
            if i >= k-1:
                results.append(v if not q else -1)
            print(i,v, prev, q, results)
            prev = v
        return results
