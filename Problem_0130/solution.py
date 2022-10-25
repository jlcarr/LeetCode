from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        
        # BFS
        queue = [(r,0) for r in range(m) if board[r][0] == 'O']
        queue += [(r,n-1) for r in range(m) if board[r][n-1] == 'O']
        queue += [(0,c) for c in range(n) if board[0][c] == 'O']
        queue += [(m-1,c) for c in range(n) if board[m-1][c] == 'O']
        queue = deque(queue)
        found = set(queue)
        
        while queue:
            r,c = queue.pop()
            for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
                ri, cj = r+i, c+j
                if (ri, cj) not in found \
                    and 0 <= ri < m \
                    and 0 <= cj < n \
                    and board[ri][cj] == 'O':
                    queue.appendleft((ri, cj))
                    found.add((ri, cj))
        
        for r in range(m):
            for c in range(n):
                if (r,c) not in found:
                    board[r][c] = 'X'

