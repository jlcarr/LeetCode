import itertools
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        acc = [0] + list(itertools.accumulate(nums))
        l = len(acc)
        j = 0
        result = 0
        for i in range(l):
            while (acc[i]-acc[j])*(i-j) >= k:
                j += 1
            result += i - j
        return result
