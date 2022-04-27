class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        #print(nums)
        
        result = []
        iprev = None
        for i in range(0, len(nums)-3):
            if nums[i] == iprev:
                continue
            jprev = None
            for j in range(i+1,len(nums)-2):
                if nums[j] == jprev:
                    continue
                L = j+1
                R = len(nums)-1
                Lprev = None
                while L < R:
                    if Lprev == nums[L]:
                        L += 1
                        continue
                    if nums[i] + nums[j] + nums[L] + nums[R] < target:
                        Lprev = nums[L]
                        L += 1
                    elif nums[i] + nums[j] + nums[L] + nums[R] > target:
                        R -= 1
                    else: #equal
                        result.append([nums[i], nums[j], nums[L], nums[R]])
                        Lprev = nums[L]
                        L += 1
                jprev = nums[j]
            iprev = nums[i]
            
        return result
