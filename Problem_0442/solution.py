class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            v = abs(nums[i])
            if nums[v-1] < 0:
                result.append(v)
            else:
                nums[v-1] *= -1
        return result
