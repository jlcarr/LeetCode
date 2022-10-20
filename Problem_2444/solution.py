class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # anything to the the last viewing of a minK and further is good
        result = 0
        last_minK = -1
        last_maxK = -1
        last_invalid = -1
        for i,n in enumerate(nums):
            if n < minK or n > maxK:
                last_minK = -1
                last_maxK = -1
                last_invalid = i
                continue
            if n == minK:
                last_minK = i
            if n == maxK:
                last_maxK = i
            # no valid sub-arrays ending here
            if last_minK == -1 or last_maxK == -1:
                continue
            # 
            last_valid = min(last_minK, last_maxK)
            result += last_valid-last_invalid
        return result
        
