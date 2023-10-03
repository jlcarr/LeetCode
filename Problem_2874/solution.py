class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        currmax = nums[-1]
        max_after = []
        for v in nums[::-1]:
            currmax = max(currmax, v)
            max_after.append(currmax)
        max_after = max_after[::-1]
        #print(max_after)
        
        currmax = nums[0]
        max_before = []
        for v in nums:
            currmax = max(currmax, v)
            max_before.append(currmax)
        #print(max_before)
        
        result = (nums[0]-nums[1])*nums[2]
        #print(result)
        for i,v in enumerate(nums):
            if i == 0 or i == len(nums)-1:
                continue
            result = max(result, (max_before[i-1] - v) * max_after[i+1])
        #print(result)
        if result < 0:
            return 0
        return result
