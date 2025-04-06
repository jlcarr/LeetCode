class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        maxlens = []
        prevs = []
        for i,iv in enumerate(nums):
            il, ip = 1, None
            for j in range(i):
                if iv % nums[j] == 0 and maxlens[j]+1 > il:
                    il = maxlens[j]+1
                    ip = j
            maxlens.append(il)
            prevs.append(ip)
        l,i = max([(l,i) for i,l in enumerate(maxlens)])
        result = [nums[i]]
        while prevs[i] is not None:
            i = prevs[i]
            result.append(nums[i])
        return result
        
