class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        atlantic_queue = [(i,n-1) for i in range(m-1)] + [(m-1,i) for i in range(n)]
        pacific_queue = [(i,0) for i in range(1,m)] + [(0,i) for i in range(n)]
        
        atlantic_found = set(atlantic_queue)
        pacific_found = set(pacific_queue)
        #print(atlantic_found)
        #print(pacific_found)
        
        for queue,found in [(atlantic_queue,atlantic_found), (pacific_queue,pacific_found)]:
            while queue:
                #print(found)
                r,c = queue.pop()
                height = heights[r][c]
                for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if r+i >= 0 and r+i < m and c+j >= 0 and c+j < n:
                        if heights[r+i][c+j] >= height:
                            if (r+i, c+j) not in found:
                                found.add((r+i, c+j))
                                queue.append((r+i, c+j))
        return list(atlantic_found & pacific_found)
                                    
