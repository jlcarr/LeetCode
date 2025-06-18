import math
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # changes = n - 1 - k
        # blocks = changes + 1
        # changes positions via stars&bars
        # elements chosen via combinatorics
        mod = 10 ** 9 + 7
        blocks = n - k
        pos = math.comb(n - 1, blocks - 1)
        if m == 1 and blocks == 1:
            return 1
        vals = m * pow(m - 1, blocks - 1, mod)
        #print(blocks, pos, vals)
        return vals * pos % mod
