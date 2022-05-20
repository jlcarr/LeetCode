class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        
        nums.append(0)
        # find streaks of non-zeroes
        streaks = []
        start = None
        has_zero = False
        for i,v in enumerate(nums):
            has_zero = has_zero or (v == 0 and i != len(nums)-1)
            if v != 0 and start is None:
                start = i
            elif v == 0 and start is not None:
                streaks.append((start, i))
                start = None
        
        for start,end in streaks:
            prod = 1
            for i in nums[start:end]:
                prod *= i
                result = max(result, prod)
            prod = 1
            for i in nums[start:end][::-1]:
                prod *= i
                result = max(result, prod)

        if has_zero and result < 0:
            return 0
        
        return result
