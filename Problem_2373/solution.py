class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return [[
            max([v for row in grid[i:i+3] for v in row[j:j+3]]) 
            for j in range(len(grid)-2)] 
        for i in range(len(grid)-2)]
