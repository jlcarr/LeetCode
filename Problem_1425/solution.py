import heapq
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        first_pos = l
        last_pos = -1
        for i,v in enumerate(nums):
            if v > 0:
                first_pos = min(first_pos, i)
                last_pos = max(last_pos, i)
        if last_pos == -1:
            return max(nums)


        l = len(nums)
        q = [(-nums[first_pos], first_pos)]
        for i in range(first_pos+1, last_pos+1):
            while q and q[0][1] + k < i:
                heapq.heappop(q)

            waspos = nums[i] >= 0

            nums[i] += max(0, -q[0][0])
            
            if waspos:
                q = []
            
            heapq.heappush(q, (-nums[i], i))
        #print(nums)
        return max(nums)
