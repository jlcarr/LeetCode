import heapq
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = len(bloomDay)
        if m * k > l:
            return -1
        starts = list(range(l))
        ends = list(range(l))
        used = [False]*l
        q = [(day,i) for i, day in enumerate(bloomDay)]
        heapq.heapify(q)
        bouquets = 0
        while q:
            day = q[0][0]
            while q and q[0][0] == day:
                _, i = heapq.heappop(q)
                if i > 0 and used[i-1] and bloomDay[i-1] <= day:
                    bouquets -= (ends[i-1]+1 - starts[i-1])//k
                    starts[i] = starts[i-1]
                if i < l-1 and used[i+1] and bloomDay[i+1] <= day:
                    bouquets -= (ends[i+1]+1 - starts[i+1])//k
                    ends[i] = ends[i+1]
                ends[starts[i]] = ends[i]
                starts[ends[i]] = starts[i]
                used[i] = True
                bouquets += (ends[i]+1 - starts[i])//k
            if bouquets >= m:
                return day
        return -2

