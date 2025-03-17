from operator import xor
from functools import reduce
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return not reduce(xor, map(lambda x: x*x+x+1,nums))
