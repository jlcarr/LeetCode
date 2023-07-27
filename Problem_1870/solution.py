import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist)-1 > int(hour) or float(len(dist)-1) == hour:
            return -1
        l, r = 1, int(math.ceil(max(dist)))
        if len(dist)-1 == int(hour) and hour-int(hour) > 0. and int(dist[-1]/(hour-int(hour))) >= r:
            r = int((dist[-1]/(hour-int(hour))))
            if sum(math.ceil(d / r) for d in dist[:-1]) + dist[-1] / r > hour:
                r += 1
            return r
        while l + 1 < r:
            m = (r + l) // 2
            #print(l,r, m, sum(math.ceil(d / m) for d in dist[:-1]) + dist[-1] / m )
            if sum(math.ceil(d / m) for d in dist[:-1]) + dist[-1] / m <= hour:
                r = m
            else:
                l = m
        #print(l,r, sum(math.ceil(d / l) for d in dist[:-1]) + dist[-1] / l )
        if sum(math.ceil(d / l) for d in dist[:-1]) + dist[-1] / l <= hour:
            return l
        return r

