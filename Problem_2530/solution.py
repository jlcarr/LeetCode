import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        score = 0
        for i in range(k):
            val = heapq.heappop(nums)
            score -= val
            heapq.heappush(nums, val // 3)
        return score

