class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # take either max normal sub-array, or complement with min-array
        n = len(nums)
        s = sum(nums)
        max_acc = nums[0]
        min_acc = -nums[0]
        result = max(s, max_acc)
        if n > 1:
            result = max(result, s+min_acc)
        for i in range(1,n):
            x = nums[i]
            max_acc = max(x, x+max_acc)
            if i < n-1:
                min_acc = max(-x, -x+min_acc)
            result = max(result, max_acc, s+min_acc)
        return result
            
