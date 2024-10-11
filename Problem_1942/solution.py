import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        available = []
        leaving_times = []
        times = sorted([(arrival, leaving, i) for i, (arrival, leaving) in enumerate(times)])
        for arrival, leaving, i in times:
            while leaving_times and leaving_times[0][0] <= arrival:
                heapq.heappush(available, heapq.heappop(leaving_times)[-1])
            if i == targetFriend:
                return available[0] if available else len(leaving_times)
            if available:
                heapq.heappush(leaving_times, (leaving, heapq.heappop(available)))
            else:
                heapq.heappush(leaving_times, (leaving, len(leaving_times)))
        return -1            
            
