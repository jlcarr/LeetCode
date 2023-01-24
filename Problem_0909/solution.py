from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        dists = [n*n*n] * (n*n)
        dists[0] = 0
        q = deque([0])
        searched = set(q)
        while q:
            curr = q.pop()
            dist = dists[curr]

            for new_curr in range(curr+1, 1+min(n*n-1, curr+6)):
                row = new_curr // n
                col = new_curr % n
                if row % 2 == 1:
                    col = n-1 - col
                #print(new_curr,'pre', row, col, board[n-1-row][col])
                if board[n-1-row][col] != -1:
                    new_curr = board[n-1-row][col]-1
                #print(new_curr,'post')

                dists[new_curr] = min(dists[new_curr], dist+1)

                if new_curr == n*n-1:
                    return dists[new_curr]

                if new_curr not in searched:
                    searched.add(new_curr)
                    q.appendleft(new_curr)
        
        #print(list(enumerate(dists)))
        if dists[n*n-1] == n*n*n:
            return -1
        return dists[n*n-1]
            
