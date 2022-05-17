class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        result = 0
        
        for r in range(len(matrix)):
            matrix[r] = list(map(int, matrix[r]))
            if r > 0:
                for i in range(len(matrix[r])):
                    if matrix[r][i] == 1:
                        matrix[r][i] += matrix[r-1][i]
            row = matrix[r]
            monostack = []
            row.append(0)
            for i, h in enumerate(row):
                while monostack and monostack[-1][1] >= h:
                    j, h_prev = monostack.pop()
                    width = i 
                    if monostack:
                        width -= monostack[-1][0]+1
                    result = max(result, h_prev*width)
                monostack.append((i,h))            
            
        return result
