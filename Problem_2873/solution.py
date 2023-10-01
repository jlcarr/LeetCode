class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        currmax = nums[-1]
        maxes = []
        for v in nums[::-1]:
            currmax = max(currmax, v)
            maxes.append(currmax)
        maxes = maxes[::-1]
        #print(maxes)
        
        result = (nums[0]-nums[1])*nums[2]
        l = len(nums)
        for i in range(l-2):
            for j in range(i+1, l-1):
                result = max(result, (nums[i]-nums[j])*maxes[j+1])
        if result < 0:
            return 0
        return result
