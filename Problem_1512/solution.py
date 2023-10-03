from collections import Counter
import math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(math.comb(v,2) for v in Counter(nums).values() if v >=2)
