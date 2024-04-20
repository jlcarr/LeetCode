class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m,n = len(land), len(land[0])

        unsearched = set([
            (i,j) 
            for i,row in enumerate(land) 
            for j,cell in enumerate(row)
            if cell == 1
        ])

        result = []
        while unsearched:
            stack = [unsearched.pop()]
            tl,br = stack[0],stack[0]
            while stack:
                i,j = stack.pop()
                tl,br = min(tl, (i,j)), max(br, (i,j))
                for ip,jp in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if (0 <= ip < m) and (0 <= jp < n) and (ip,jp) in unsearched:
                        unsearched.remove((ip,jp))
                        stack.append((ip,jp))
            result.append([*tl,*br])
        
        return result
