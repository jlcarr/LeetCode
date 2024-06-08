class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        prev = 0
        prevs = set()
        cumsum = 0
        for i in nums:
            cumsum = (cumsum + i) % k
            complement = (-cumsum) % k
            #print(cumsum, complement)
            if complement in prevs:
                return True
            prevs.add(prev)
            prev = complement
        return False

