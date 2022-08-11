class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        end = points[0][0]-1
        result = 0
        for p in points:
            if p[0] > end:
                end = p[1]
                result += 1
                
        return result

