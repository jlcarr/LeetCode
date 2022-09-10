import scipy.spatial
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances, indices = scipy.spatial.KDTree(points).query([0,0], k=k)
        if k == 1:
            return [points[indices]]
        return [points[i] for i in indices]
