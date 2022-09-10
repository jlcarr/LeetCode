class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        s = [(p[0]*p[0] + p[1]*p[1],i) for i,p in enumerate(points)]
        s.sort()
        return [points[p[1]] for p in s[:k]]
