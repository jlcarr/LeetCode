class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        tot = sum(nums)
        if tot % k != 0:
            return False
        target = tot // k
        rems = [target]*k
        
        def rec(i):
            if i == len(nums): # can only reach the end if all are assigned
                return True
            for j in range(k):
                if nums[i] <= rems[j]:
                    rems[j] -= nums[i]
                    if rec(i+1):
                        return True
                    rems[j] += nums[i]
                if rems[j] == target:
                    break
            return False
        
        return rec(0)
