class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2
        
        if target in nums:
            return True
        
        possibs = set()
        for n in nums:
            for prev in possibs.copy():
                if n+prev == target:
                    return True
                possibs.add(n+prev)
            possibs.add(n)
        return False
