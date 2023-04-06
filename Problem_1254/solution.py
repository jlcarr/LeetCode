class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        indices = set([(r,c) for r in range(rows) for c in range(cols)])
        result = 0
        while indices:
            r,c = indices.pop()
            if grid[r][c] == 1:
                continue

            is_island = True
            q = [(r,c)]
            while q:
                r,c = q.pop()
                for p in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                    rp,cp = p
                    if not (0 <= rp < rows) or not (0 <= cp < cols):
                        is_island = False
                        continue
                    p = (rp,cp)
                    if p in indices:
                        indices.remove(p)
                        if grid[rp][cp] == 0:
                            q.append(p)
            if is_island:
                result += 1

        return result
