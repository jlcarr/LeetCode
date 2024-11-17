import bisect
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # min i+1-j | j<=i | cumsum[i+1] - cumsum[j] >= k
        # for each i: max j | cumsum[i+1] - k >= cumsum[j]
        # q in order, increasing, since we can tighten
        cumsum = [0]
        for i in range(len(nums)):
            cumsum.append(cumsum[-1] + nums[i])
        
        result = -1
        q = [(0,-1)]
        for i in range(len(nums)):
            while q and q[-1][0] >= cumsum[i+1]:
                q.pop()
            q.append((cumsum[i+1],i))
            jj = bisect.bisect_left(q,(cumsum[i+1]-k,-2))
            if cumsum[i+1]-k < q[jj][0] and jj > 0 and cumsum[i+1]-k >= q[jj-1][0]:
                jj -= 1
            #print(q, jj, cumsum[i+1]-k)
            if cumsum[i+1]-k >= q[jj][0]:
                if result == -1:
                    result = i+1 - q[jj][1]
                result = min(result, i - q[jj][1])
        
        return result


