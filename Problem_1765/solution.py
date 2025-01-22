class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        q = [(i,j) for i,row in enumerate(isWater) for j,c in enumerate(row) if c]
        result = [[c-1 for c in row] for row in isWater]
        height = 0
        while q:
            height += 1
            newq = []
            for i,j in q:
                for ip,jp in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if (0 <= ip < m) and (0 <= jp < n) and result[ip][jp] == -1:
                        result[ip][jp] = height
                        newq.append((ip,jp))
            q = newq
        return result
