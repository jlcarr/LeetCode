import bisect
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def check(k):
            prefix = [0] * len(nums)
            for l,r,val in queries[:k]:
                prefix[l] += val
                if r+1 < len(nums):
                    prefix[r+1] -= val
            acc = 0
            for p,n in zip(prefix,nums):
                acc += p
                if n > acc:
                    return False
            return True
            if sat:
                j = k-1
            else:
                i = k+1
        result = bisect.bisect_left(range(len(queries)+1), True, key=check)
        if result > len(queries):
            return -1
        return result
