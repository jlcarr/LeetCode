class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1)
        i = 1
        prev_pow = 1
        while i <= n:
            if i == prev_pow << 1:
                prev_pow = prev_pow << 1
            result[i] = 1 + result[i-prev_pow]
            i += 1
        return result
