class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = 0
        l, r = 0,-1
        curr_sum = 0
        while l < len(nums)-1:
            #print(l,r)
            if curr_sum < target and r < len(nums)-1:
                # increment right
                r += 1
                curr_sum += nums[r]
            else:
                # increment left
                curr_sum -= nums[l]
                l += 1
                if l > r:
                    r = l
                    curr_sum += nums[r]
            # update solution
            curr_len = r+1 - l
            if curr_sum >= target and (curr_len < result or result == 0):
                result = curr_len
        return result
