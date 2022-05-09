class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        
        def search(i, j, pos, searched=set()):
            if board[i][j] != word[pos]:
                return False
            if pos == len(word)-1:
                return True
            
            searched = searched.copy()
            searched.add((i,j))
            
            # up
            if i > 0 and (i-1, j) not in searched \
                and search(i-1, j, pos+1, searched):
                return True
            # down
            if i < m-1 and (i+1, j) not in searched \
                and search(i+1, j, pos+1, searched):
                return True
            # left
            if j > 0 and (i, j-1) not in searched \
                and search(i, j-1, pos+1, searched):
                return True
            # right
            if j < n-1 and (i, j+1) not in searched \
                and search(i, j+1, pos+1, searched):
                return True
            
            return False
        
        for i in range(m):
            for j in range(n):
                if search(i, j, 0):
                    return True
        return False
