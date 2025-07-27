class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        nex = 0
        result = 0
        while nex < len(nums):
            while curr < len(nums) and nums[curr] == nums[prev]:
                curr += 1
            nex = curr
            while nex < len(nums) and nums[nex] == nums[curr]:
                nex += 1
            if nex < len(nums):
                result += int(nums[prev] < nums[curr] > nums[nex])
                result += int(nums[prev] > nums[curr] < nums[nex])
            prev = curr
        return result
            


