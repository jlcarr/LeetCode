from functools import cache
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def rec(l,r):
            turn = ((r - l - len(nums)) % 2) * 2 - 1
            if l == r:
                #print(l,r,turn,turn * nums[l])
                return turn * nums[l]
            f = max if turn > 0 else min
            result = rec(l+1, r) + turn * nums[l]
            result = f(result, rec(l, r-1) + turn * nums[r])
            #print(l,r,turn, result)
            return result
        
        return rec(0, len(nums)-1) >= 0
