class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        v = set()
        for i in nums:
            if i in v:
                return True
            v.add(i)
        return False
