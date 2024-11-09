class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        result = 0
        mask = 1
        while (x >= mask) | n:
            #print(result, mask, x, n)
            if x & mask:
                result |= mask
            else:
                if n & 1:
                    result |= mask
                n >>= 1
            mask <<= 1
        return result
