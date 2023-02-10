import numpy as np
from scipy import ndimage
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        grid = np.array(grid)
        if grid.max() != 1 or grid.min() != 0:
            return -1
        return ndimage.distance_transform_cdt(1-grid, metric='taxicab').max()
