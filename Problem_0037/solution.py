class Solution:        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.board = board
        self.indices = [(r,c) for r in range(9) for c in range(9) if board[r][c] == '.']
        
        def feasibleStep(r,c,v):
            return all([self.board[r][i] != v for i in range(9)]) and \
                all([self.board[i][c] != v for i in range(9)]) and \
                all([self.board[i][j] != v for i in range(r//3*3,r//3*3+3) for j in range(c//3*3,c//3*3+3)])
        
        # solve with DFS, checking constraints on each level
        def dfs(depth=0):
            if depth == len(self.indices):
                return True
            r,c = self.indices[depth]
            for v in map(str,range(1,9+1)):
                if feasibleStep(r,c,v):
                    self.board[r][c] = v
                    if dfs(depth+1):
                        return True
            self.board[r][c] = '.'
            return False
        
        dfs()
        
