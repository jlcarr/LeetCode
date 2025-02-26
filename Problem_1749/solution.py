class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        acc = 0
        max_acc = 0
        min_acc = 0
        result = 0
        for v in nums:
            acc += v
            max_acc = max(max_acc, acc)
            min_acc = min(min_acc, acc)
            result = max(result, max_acc - min_acc)
        return result

