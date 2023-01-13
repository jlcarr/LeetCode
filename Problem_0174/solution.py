class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon), len(dungeon[0])
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if r < m-1 and c < n-1:
                    dungeon[r][c] = -dungeon[r][c] + min(
                        dungeon[r+1][c],
                        dungeon[r][c+1]
                        )
                elif r == m-1 and c < n-1:
                    dungeon[r][c] = -dungeon[r][c] + dungeon[r][c+1]
                elif r < m-1 and c == n-1:
                    dungeon[r][c] = -dungeon[r][c] + dungeon[r+1][c]
                elif r == m-1 and c == n-1:
                    dungeon[r][c] = -dungeon[r][c]
                dungeon[r][c] = max(dungeon[r][c], 0)
        
        #for row in dungeon:
        #    print(row)

        return dungeon[0][0]+1
