class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        #print(nums)
        
        result = sum(nums[:3])
        iprev = None
        for i in range(0, len(nums)-2):
            if nums[i] == iprev:
                continue
            L = i+1
            R = len(nums)-1
            Lprev = None
            while L < R:
                if Lprev == nums[L]:
                    L += 1
                    continue
                diff = nums[i] + nums[L] + nums[R] - target
                if abs(diff) < abs(result-target):
                    result = nums[i] + nums[L] + nums[R]
                if diff < 0:
                    Lprev = nums[L]
                    L += 1
                elif diff > 0:
                    R -= 1
                else: #equal
                    return target
            iprev = nums[i]
            
        return result
