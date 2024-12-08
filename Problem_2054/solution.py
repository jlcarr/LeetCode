import heapq
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        q = []
        result = 0
        maxPrevValue = 0
        for startTime, endTime, value in events:
            while q and q[0][0] < startTime:
                maxPrevValue = max(maxPrevValue, heapq.heappop(q)[1])
            result = max(result, value+maxPrevValue)
            heapq.heappush(q, (endTime,value))
        return result
