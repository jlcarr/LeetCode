class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        result = 0
        avail = 1
        meetings.sort()
        for s,e in meetings:
            result += max(0, s - avail)
            avail = max(avail, e+1)
        return result + max(0, days+1 - avail)
