class Solution:
    def check(self, nums: List[int]) -> bool:
        unsorted = int(nums[-1] > nums[0])
        for i in range(len(nums)-1):
            unsorted += int(nums[i] > nums[i+1])
            if unsorted > 1:
                return False
        return True
