class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        downval = 0
        upval = sum(grid[0])
        result = upval
        for u,d in zip(*grid):
            upval -= u
            result = min(result, max(upval, downval))
            downval += d
        return result
