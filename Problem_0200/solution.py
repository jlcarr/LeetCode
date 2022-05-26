class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        to_search = set([(i,j) for i in range(m) for j in range(n) if grid[i][j] == '1'])
        
        result = 0
        while to_search:
            result += 1
            queue = [to_search.pop()]
            while queue:
                i,j = queue.pop()
                for i_p,j_p in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if  (i+i_p, j+j_p) in to_search:
                        to_search.remove((i+i_p, j+j_p))
                        queue.append((i+i_p, j+j_p))
        return result
