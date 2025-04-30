import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(int(math.log10(i)) & 1 for i in nums)
