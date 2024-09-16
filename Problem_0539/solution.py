class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [int(t[:2])*60+int(t[-2:]) for t in timePoints]
        timePoints.sort()
        endpoint = 24*60+timePoints[0]-timePoints[-1]
        return min([t2-t1 for t2,t1 in zip(timePoints[1:],timePoints[:-1])]+[endpoint])
