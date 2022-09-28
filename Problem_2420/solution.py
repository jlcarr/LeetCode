class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        result = []
        n = len(nums)
        if k == 1:
            return [i for i in range(k, n-k)]
        if 2*k+1 > n:
            return []
        noninc = []
        nondec = []
        for i in range(n-1):
            noninc.append(int(nums[i] >= nums[i+1]))
            nondec.append(int(nums[i] <= nums[i+1]))
        noninc.append(1)
        nondec.append(1)
        noninc_count = sum(noninc[0:k-1])
        nondec_count = sum(nondec[k+1:2*k])
        if noninc_count == k-1 and nondec_count == k-1:
            result.append(k)
        #print(noninc, nondec)
        #print(noninc_count, nondec_count)
        # main
        for i in range(k+1, n-k):
            noninc_count += noninc[i-2] - noninc[i-k-1]
            nondec_count += nondec[i+k-1] - nondec[i]
            if noninc_count == k-1 and nondec_count == k-1:
                result.append(i)
            #print(i, noninc_count, nondec_count)
        return result
