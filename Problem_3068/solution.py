class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        result = sum(max(i,i^k) for i in nums)
        count = sum(i<i^k for i in nums)
        if count % 2 == 0:
            return result
        return result - min(abs(i-(i^k)) for i in nums)
