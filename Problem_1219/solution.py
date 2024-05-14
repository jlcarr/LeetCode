class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # state = pos, cells = m * n * g = 15 * 15 * 25
        self.result = 0
        self.subresult = 0
        self.grid = grid
        def rec(i,j):
            self.result = max(self.result, self.subresult)
            for ip,jp in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if (0 <= ip < len(self.grid)) \
                    and (0 <= jp < len(self.grid[0])) \
                    and self.grid[ip][jp] != 0:
                    temp = self.grid[ip][jp]
                    self.subresult += temp
                    self.grid[ip][jp] = 0
                    rec(ip,jp)
                    self.grid[ip][jp] = temp
                    self.subresult -= temp

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if grid[i][j] != 0:
                    temp = self.grid[i][j]
                    self.subresult += temp
                    self.grid[i][j] = 0
                    rec(i,j)
                    self.grid[i][j] = temp
                    self.subresult -= temp
        return self.result
