class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        result = 0
        for p12 in [(0,0),(0,1),(1,0),(1,1)]:
            subseqi = 0
            for n in nums:
                if n % 2 == p12[subseqi%2]:
                    subseqi += 1
            result = max(result, subseqi)
        return result
