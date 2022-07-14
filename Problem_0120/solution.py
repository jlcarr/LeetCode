class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(1,len(triangle)):
            for i in range(r+1):
                if i == 0:
                    triangle[r][i] += triangle[r-1][i]
                elif i == r:
                    triangle[r][i] += triangle[r-1][i-1]
                else:
                    triangle[r][i] += min(triangle[r-1][i-1], triangle[r-1][i])
        return min(triangle[-1]) 
