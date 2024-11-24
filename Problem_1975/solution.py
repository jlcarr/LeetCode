class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        tot = sum([abs(c) for row in matrix for c in row])
        count = sum([c < 0 for row in matrix for c in row])
        if count % 2 == 0:
            return tot
        return tot - 2 * min([abs(c) for row in matrix for c in row])
