class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        maxv = max(nums)
        bitlen = 0
        while maxv:
            maxv >>= 1
            bitlen += 1
        if k >= (1 << bitlen):
            return -1
        #print(bitlen)

        result = len(nums) + 1
        bitcounts = [0] * bitlen
        l,lv = 0,nums[0]
        for r,rv in enumerate(nums):
            # add new right value
            ibit = 0
            while rv:
                bitcounts[ibit] += rv & 1
                rv >>= 1
                ibit += 1
            # check new solution
            curr = sum((bitcounts[ibit] > 0) * (1 << ibit) for ibit in range(bitlen))
            #print(curr)
            if curr >= k:
                result = min(result, r - l + 1)
            # tighten left
            while curr >= k and l < r:
                # remove current lv
                ibit = 0
                while lv:
                    bitcounts[ibit] -= lv & 1
                    lv >>= 1
                    ibit += 1
                l += 1
                lv = nums[l]
                curr = sum((bitcounts[ibit] > 0) * (1 << ibit) for ibit in range(bitlen))
                #print(curr, r - l + 1)
                if curr >= k:
                    result = min(result, r - l + 1)
            #print(l,r,bitcounts, result)
        if result == len(nums) + 1:
            return -1
        return result
