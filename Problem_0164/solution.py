class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        minv = min(nums)
        maxv = max(nums)
        if minv == maxv:
            return 0
        n = len(nums)
        buckets = []
        for i in range(n):
            buckets.append([])

        for v in nums:
            index = int((v-minv)/(maxv-minv) * n)
            index = min(index, n-1)
            buckets[index].append(v)
        
        result = 0
        prevmax = minv
        for bucket in buckets:
            if not bucket:
                continue
            minbucket = min(bucket)
            result = max(result, minbucket-prevmax)
            prevmax = max(bucket)

        return result
