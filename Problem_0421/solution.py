class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        result = 0
        
        n = len(f"{max(nums):b}")
        for i in range(n):
            result *= 2
            prefixes = set([num >> (n-1-i) for num in nums])
            for pref in prefixes:
                if pref ^ (result+1) in prefixes:
                    result += 1
                    break
        return result
        
