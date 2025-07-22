class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cumsum = nums[0]
        window = {cumsum}
        l = 0
        result = cumsum
        for r in range(1,len(nums)):
            while nums[r] in window:
                window.remove(nums[l])
                cumsum -= nums[l]
                l += 1
            window.add(nums[r])
            cumsum += nums[r]
            result = max(result, cumsum)
        return result

