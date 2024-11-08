class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maxv = (1 << maximumBit) - 1

        cumxor = 0
        for i in nums:
            cumxor ^= i

        result = []
        while nums:
            result.append((cumxor & maxv) ^ maxv)
            cumxor ^= nums.pop()
        return result 
