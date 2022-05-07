class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = []
        for i in range(n):
            result.append([0]*n)
        
        counter = 1
        spirals = 0
        while spirals*2 < n:
            if spirals*2+1 == n:
                result[spirals][spirals] = counter
                break
            # top
            for i in range(n-1-2*spirals):
                result[spirals][spirals+i] = counter
                counter += 1
            # right
            for i in range(n-1-2*spirals):
                result[spirals+i][-1-spirals] = counter
                counter += 1
            # bottom
            for i in range(n-1-2*spirals):
                result[-1-spirals][-1-i-spirals] = counter
                counter += 1
            # left
            for i in range(n-1-2*spirals):
                result[-1-i-spirals][spirals] = counter
                counter += 1
            spirals += 1
            
        return result
            
