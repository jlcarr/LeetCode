from functools import reduce
from operator import xor
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cumxor = reduce(xor, nums)
        temp = cumxor
        mask = 1
        while temp % 2 == 0:
            temp >>= 1
            mask <<= 1
        first = reduce(xor, [i for i in nums if i & mask])
        return [first, first ^ cumxor]
