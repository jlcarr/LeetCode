class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(numRows-1):
            result.append([1] + [i+j for i,j in zip(result[-1][:-1],result[-1][1:])] + [1])
        return result
