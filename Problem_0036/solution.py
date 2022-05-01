class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in board:
            found = set()
            for c in r:
                if c != '.' and c in found:
                    return False
                found.add(c)
        # check cols
        for c in range(len(board)):
            found = set()
            for r in range(len(board)):
                if board[r][c] != '.' and board[r][c] in found:
                    return False
                found.add(board[r][c])
                
        # check sub-box
        for i_box in range(3):
            for j_box in range(3):
                found = set()
                for r in range(3):
                    for c in range(3):
                        val = board[i_box*3+r][j_box*3+c]
                        if val != '.' and val in found:
                            return False
                        found.add(val)
        return True
