import hashlib
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rs = dict()
        # rows
        for i in range(n):
            m = hashlib.sha256()
            for j in range(n):
                m.update(grid[i][j].to_bytes(length=8, byteorder='big'))
            d = m.digest()
            if d not in rs:
                rs[d] = set()
            rs[d].add(i)
        result = 0
        #cols
        for i in range(n):
            m = hashlib.sha256()
            for j in range(n):
                m.update(grid[j][i].to_bytes(length=8, byteorder='big'))
            d = m.digest()
            if d in rs:
                for r in rs[d]:
                    #result.append((r, i))
                    result += 1
        return result
