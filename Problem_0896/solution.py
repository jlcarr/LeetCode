class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        prev = nums[0]
        for n in nums:
            inc = inc and (n >= prev)
            dec = dec and (n <= prev)
            if not inc and not dec:
                return False
            prev = n
        
        return True
