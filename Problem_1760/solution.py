class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l,r = 1, max(nums)
        while l < r:
            mid = (r+l)//2
            # compute ops
            ops = 0
            for v in nums:
                # mid * (ops+1) >= v
                # ops >= v // mid - 1
                ops += (v-1) // mid
            if ops > maxOperations:
                l = mid + 1
            else:
                r = mid
        return l
