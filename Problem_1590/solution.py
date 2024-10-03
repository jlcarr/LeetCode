class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # target - (acc - rems) = 0
        # rems = acc - target
        target = sum(nums) % p
        if target == 0:
            return 0
        #print(target)
        result = len(nums)
        rems = {0:-1}
        acc = 0
        for i,v in enumerate(nums):
            acc += v
            acc %= p
            r = (acc - target) % p
            if r in rems:
                result = min(result, i-rems[r])
            rems[acc] = i
            #print(i,v, acc, r, rems)
        if result < len(nums):
            return result
        return -1
        
