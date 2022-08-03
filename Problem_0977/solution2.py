class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for pos in range(l):
            if nums[pos] >= 0:
                break
        neg = pos-1
        
        result = []
        while neg >= 0 and pos < l:
            if nums[pos]*nums[pos] < nums[neg]*nums[neg]:
                result.append(nums[pos]*nums[pos])
                pos += 1
            else:
                result.append(nums[neg]*nums[neg])
                neg -= 1
        while neg >= 0:
            result.append(nums[neg]*nums[neg])
            neg -= 1
        while pos < l:
            result.append(nums[pos]*nums[pos])
            pos += 1

        return result
