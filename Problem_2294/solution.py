class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 1
        prev = nums[0]
        for v in nums:
            if v - prev > k:
                result += 1
                prev = v
        return result
