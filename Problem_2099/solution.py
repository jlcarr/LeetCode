import operator
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        return list(map(operator.itemgetter(1), sorted(sorted(enumerate(nums), key=operator.itemgetter(1))[-k:])))
