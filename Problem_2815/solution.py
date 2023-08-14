class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_digits = [list(str(i)) for i in nums]
        max_digits = [int(max(i)) for i in max_digits]
        dig_sets = {i:[] for i in range(10)}
        for i,d in zip(nums,max_digits):
            dig_sets[d].append(i)
        result = -1
        for d in dig_sets.values():
            l = len(d)
            for i in range(l):
                for j in range(i+1,l):
                    result = max(result, d[i]+d[j])
        return result
