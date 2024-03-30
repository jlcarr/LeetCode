class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxn = max(nums)
        result = 0

        wcount = 0
        l = 0
        for r,n in enumerate(nums):
            if n == maxn:
                wcount += 1
            while wcount > k and l < r:
                if nums[l] == maxn:
                    wcount -= 1
                l +=1
            while nums[l] != maxn:
                l +=1
            if wcount == k:
                result += l+1

        return result
