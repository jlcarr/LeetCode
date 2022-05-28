class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort()
        curr_end = intervals.pop(0)[-1]
        for i in intervals:
            if i[0] >= curr_end:
                curr_end = i[-1]
            else:
                curr_end = min(curr_end, i[-1])
                result += 1
        return result
