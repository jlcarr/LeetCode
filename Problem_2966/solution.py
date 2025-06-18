class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        #print([nums[3*i+2] - nums[3*i] > k for i in range(len(nums)//3)])
        if any(nums[3*i+2] - nums[3*i] > k for i in range(len(nums)//3)):
            return []
        return [[nums[3*i+j] for j in range(3)] for i in range(len(nums)//3)]
