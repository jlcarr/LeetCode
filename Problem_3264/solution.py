import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        q = [(v,i) for i,v in enumerate(nums)]
        heapq.heapify(q)
        for ik in range(k):
            v,i = heapq.heappop(q)
            nums[i] = v * multiplier
            heapq.heappush(q, (v * multiplier, i))
        return nums
