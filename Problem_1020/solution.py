class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        indices = set([(r,c) for r in range(rows) for c in range(cols)])
        result = 0
        while indices:
            r,c = indices.pop()
            if grid[r][c] == 0:
                continue
            q = [(r,c)]
            size = 1
            is_island = True
            while q:
                r,c = q.pop()
                for ri,ci in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if not (0 <= ri < rows) or not (0 <= ci < cols):
                        is_island = False
                        continue
                    if (ri,ci) not in indices:
                        continue
                    indices.remove((ri,ci))
                    if grid[ri][ci] == 0:
                        continue
                    q.append((ri,ci))
                    size += 1
            if is_island:
                result += size
        return result
