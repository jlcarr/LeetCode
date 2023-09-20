class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l = len(nums)
        cumsum = 0
        poses = {0: 0}
        for i,n in enumerate(nums):
            cumsum += n
            if cumsum not in poses:
                poses[cumsum] = i+1
        
        result = len(nums)+1
        if x in poses:
            result = poses[x]
        for i, n in enumerate(nums[::-1]):
            x -= n
            if x in poses and poses[x] < l-1-i:
                result = min(result, poses[x] + i+1)

        if result == len(nums)+1:
            return -1
        return result
