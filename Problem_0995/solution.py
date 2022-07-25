from collections import deque
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        result = 0
        end_flips = deque()
        for i in range(len(nums)):
            if end_flips and end_flips[-1] == i: # pop out
                end_flips.pop()
                
            if len(end_flips) % 2 == 1:
                nums[i] = 1 - nums[i]
            
            if nums[i] == 0:
                if i >= len(nums)-k+1:
                    return -1
                end_flips.appendleft(i+k)
                nums[i] = 1 - nums[i]
                result += 1
            #print(i, nums, end_flips, result)
        
        return result
