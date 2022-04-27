class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)
        
        result = []
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
                if nums[i] + nums[L] + nums[R] < 0:
                    Lprev = nums[L]
                    L += 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                else: #equal
                    result.append([nums[i], nums[L], nums[R]])
                    Lprev = nums[L]
                    L += 1
            iprev = nums[i]
            
        return result
