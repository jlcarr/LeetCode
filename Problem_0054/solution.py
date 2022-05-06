class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        while True:
            # top
            while len(matrix[0]) > 0:
                result.append(matrix[0].pop(0))
            matrix.pop(0)
            if len(matrix) == 0:
                return result
            
            # right
            for r in range(len(matrix)):
                result.append(matrix[r].pop())
            if len(matrix[0]) == 0:
                return result
            
            # bottom
            while len(matrix[-1]) > 0:
                result.append(matrix[-1].pop())
            matrix.pop()
            if len(matrix) == 0:
                return result
            
            # left
            for r in range(len(matrix)):
                result.append(matrix[len(matrix)-1-r].pop(0))
            if len(matrix[0]) == 0:
                return result
            
