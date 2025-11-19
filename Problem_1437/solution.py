class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last1 = -k-2
        for i,v in enumerate(nums):
            if v:
                if i - last1 <= k:
                    return False
                last1 = i
        return True
