class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        length = len(nums)
        currmin = nums[k]
        result = currmin
        i,j = k,k
        while i > 0 or j < length-1:
            while i > 0 and nums[i-1] >= currmin:
                i -= 1
            while j < length-1 and nums[j+1] >= currmin:
                j += 1
            #print(i,j, currmin)
            result = max(result, currmin*(j-i+1))
            if i > 0 and j < length-1:
                currmin = min(currmin, max(nums[max(0,i-1)], nums[min(length-1,j+1)]))
            elif i > 0:
                currmin = min(currmin, nums[i-1])
            elif j < length-1:
                currmin = min(currmin, nums[j+1])
        return result
