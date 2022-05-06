class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        # binary search for start
        L, R = 0, len(intervals)
        while L+1 < R:
            M = (R+L)//2
            if intervals[M][0] > newInterval[0]:
                R = M
            else:
                L = M
        
        #print(L)
        
        # merge all applicable
        result = intervals[:L]
        intervals = intervals[L:]
        
        #print(result, intervals)
        
        if intervals[0][-1] < newInterval[0]:
            result.append(intervals.pop(0))
        elif newInterval[-1] >= intervals[0][0]:
            newInterval[0] = min(newInterval[0], intervals[0][0])
            newInterval[-1] = max(newInterval[-1], intervals[0][-1])
            intervals.pop(0)
        
        #print(result, intervals, newInterval)
        
        while intervals and newInterval[-1] >= intervals[0][0]:
            newInterval[-1] = max(newInterval[-1], intervals.pop(0)[-1])
            
        #print(result, intervals, newInterval)
        
        result += [newInterval] + intervals
        
        return result
                
