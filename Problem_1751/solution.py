import heapq
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        result = 0
        events.sort()
        dayKValues = dict() # day -> k -> sumvalue
        nextIndices = []
        for (startDay, endDay, value) in events:
            # move all trailing up
            while nextIndices and nextIndices[0] < startDay:
                if startDay not in dayKValues: # start new record if needed
                    heapq.heappush(nextIndices, startDay)
                    dayKValues[startDay] = dict()
                index = heapq.heappop(nextIndices)
                for cumk, cumvalue in dayKValues[index].items(): # move up the prev
                    curr = dayKValues[startDay].get(cumk, 0)
                    dayKValues[startDay][cumk] = max(curr, cumvalue)
                    result = max(result, dayKValues[startDay][cumk])
                del dayKValues[index] # remove the old record
            # add the new event
            if endDay+1 not in dayKValues: # start new record if needed
                heapq.heappush(nextIndices, endDay+1)
                dayKValues[endDay+1] = dict()
            # what happens if use
            curr = dayKValues[endDay+1].get(k-1, 0)
            dayKValues[endDay+1][k-1] = max(curr, value)
            result = max(result, dayKValues[endDay+1][k-1])
            if startDay in dayKValues:
                for cumk, cumvalue in dayKValues[startDay].items(): # move up the prev
                    if cumk > 0:
                        curr = dayKValues[endDay+1].get(cumk-1, 0)
                        dayKValues[endDay+1][cumk-1] = max(curr, cumvalue+value)
                        result = max(result, dayKValues[endDay+1][cumk-1])
        return result
