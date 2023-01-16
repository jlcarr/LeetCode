from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sol = ''.join(
            sorted(
                [str(n) for n in nums], 
                key=cmp_to_key(lambda x,y: int(x+y) - int(y+x)),
                reverse=True
            )
        )
        if sol.startswith('0'):
            return '0'
        return sol
