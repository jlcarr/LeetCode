class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0
        for i in arr:
            if i - prev > 1:
                i = prev + 1
            prev = i
        
        return prev
