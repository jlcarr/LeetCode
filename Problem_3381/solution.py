class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        result = sum(nums[:k])
        curr = [0] * k
        minc = [sum(map(abs,nums))] * k
        minc[k-1] = 0
        for i,v in enumerate(nums):
            curr[i%k] = curr[(i-1)%k] + v
            if i >= k-1:
                result = max(result, curr[i%k] - minc[i%k])
            minc[i%k] = min(minc[i%k], curr[i%k])
            #print(i,v,result, curr, minc)
        return result
