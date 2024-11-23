class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m,n = len(box),len(box[0])
        result = [['.']*m for col in range(n)]
        for irow in range(m):
            curr_count = 0
            for icol in range(n+1):
                if icol < n and box[irow][icol] == '#':
                    curr_count += 1
                if icol == n or box[irow][icol] == '*':
                    if icol < n:
                        result[icol][m-1-irow] = '*'
                    for iicol in range(icol-curr_count,icol):
                        result[iicol][m-1-irow] = '#'
                    curr_count = 0
        return result
