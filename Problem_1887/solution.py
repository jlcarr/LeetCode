class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        prev = nums[0]
        steps = 0
        result = 0
        for num in nums:
            if num != prev:
                steps += 1
            result += steps
            prev = num
        return result
